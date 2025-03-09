from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _t
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import aget_user

from common.auth import aclient_required, ensure_for_current_user
from common.django_utils import alogout, arender
from common.forms import CustomPasswordChangeForm

from .models import Subscription, PlanChoice
from writer.models import Article
from . import paypal as sub_manager
from .forms import UpdateSubscriptionForm, UpdateUserForm

@aclient_required
async def dashboard(resquest: HttpRequest) -> HttpResponse:
    
    user = await aget_user(resquest)
    subscription_plan = 'no subscription yet'
    if subscription := await Subscription.afor_user(user):
        
        subscription_plan = (await subscription.aplan_choice()).name
        if not subscription.is_active:
            subscription_plan += ' (inactive)'
    
    context = {'subscription_plan': subscription_plan}
    return await arender(resquest, 'client/dashboard.html', context)


@aclient_required
async def browse_articles(resquest: HttpRequest) -> HttpResponse:
    
    user = await aget_user(resquest)
    articles = []
    
    if subscription := await Subscription.afor_user(user):
        if not await subscription.ais_premium():
            articles = Article.objects.filter(is_premium = False)
            
        else:
            articles =Article.objects.all()
    

    context = {'has_subscription': subscription is not None, 'articles': articles}
    return await arender(resquest, 'client/browse-articles.html', context)



@aclient_required
async def subscription_plan(resquest: HttpRequest) -> HttpResponse:
    
    user = await aget_user(resquest)
    
    if await Subscription.afor_user(user):
        return redirect('client-dashboard')
    
    context = { "plan_choices": PlanChoice.objects.filter(is_active = True) }
    
    
    return await arender(resquest, 'client/subscription-plan.html', context)


@aclient_required
async def subscribe_plan(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    if await Subscription.afor_user(user):
        return redirect('client-dashboard')
    context = {'plan_choices': PlanChoice.objects.filter(is_active = True)}
    return await arender(request, 'client/subscribe-plan.html', context)


@aclient_required
async def update_client(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    subscription_plan = ''
    
    # Get the user's subscription if it exists
    subscription = await Subscription.afor_user(user)
    if subscription:
        subscription_plan = (await subscription.aplan_choice()).name

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)

        if await form.ais_valid():
            await form.asave()
            return redirect('client-dashboard')
    else:
        form = UpdateUserForm(instance=user)

    context = {
        'update_user_form': form,
        'has_subscription': bool(subscription),
        'subscription': subscription,
        'subscription_plan': subscription_plan,
    }

    return await arender(request, 'client/update-client.html', context)


@aclient_required
async def create_subscription(request: HttpRequest, sub_id: str, plan_code: str) -> HttpResponse:
    
    user = await aget_user(request)
    
    if await Subscription.afor_user(user):
        return redirect('client-dashboard')
    
    
    plan_choice = await PlanChoice.afrom_plan_code(plan_code)
    
    await Subscription.objects.acreate(
        plan_choice = plan_choice,
        cost = plan_choice.cost,
        external_subscription_id = sub_id,
        is_active = True,
        user = user,
    )
    
    
    context = {'subscription_plan': plan_choice.name}
    return await arender(request, 'client/create-subscription.html', context)


@aclient_required
@ensure_for_current_user(Subscription, redirect_if_missing = 'client-dashboard')
async def cancel_subscription(request: HttpRequest, subscription: Subscription) -> HttpResponse:
    
    if request.method == 'POST':
        access_token = await sub_manager.get_access_token()
        sub_id = subscription.external_subscription_id
        
        await sub_manager.cancel_subscription(access_token, sub_id)
        
        await subscription.adelete()
        
        context = {}
        
        template = 'client/cancel-subscription-confirmed.html'
        
        return await arender(request, 'client/cancel-subscription-confirmed.html')
    
    else:
        context = {'subscription_plan': (await subscription.aplan_choice()).name}
        template = 'client/cancel-subscription.html'
        
    return await arender(request, template, context)


@aclient_required
@ensure_for_current_user(Subscription, redirect_if_missing = 'client-dashboard')
async def update_subscription(request: HttpRequest, subscription: Subscription) -> HttpResponse:
    
    user_plan_choice = await subscription.aplan_choice()
    
    if request.method == 'POST':
        new_plan_code =  request.POST['plan_choices']
        new_plan_choice = await PlanChoice.afrom_plan_code(new_plan_code)
        new_plan_id = new_plan_choice.external_plan_id
        
        access_token = await sub_manager.get_access_token()
        approval_url =  await sub_manager.update_subscription(
            access_token,
            subscription_id = subscription.external_subscription_id,
            new_plan_id = new_plan_id,
            return_url = request.build_absolute_uri(reverse('update-subscription-confirmed')),
            cancel_url = request.build_absolute_uri(reverse('update-client')),
        )
        
        
        print(f"[+] approbal url: {approval_url}")
        
        if approval_url:
            http_response = redirect(approval_url)
            request.session['subscription.id'] = subscription.id
            request.session['new_plan_id'] = new_plan_id
        
        else:
            error_msg = 'Error unable to obtain approval link from PayPal'
            http_response = HttpResponse(error_msg)
        
    
    else:
        form = await UpdateSubscriptionForm.ainit(
            exclude = [user_plan_choice.plan_code],
            format_fn = lambda pc: _t(f'{pc.name} ({pc.cost} / monthly)'),
        )
        
        context = { 'update_subscription_form': form }
        
        http_response = await arender(request, 'client/update-subscription.html', context)
        
        
        
    return http_response


@aclient_required
async def update_subscription_confirmed(request: HttpRequest) -> HttpResponse:
    session = request.session
    
    try:
        subscription_db_id = session['subscription.id']
        new_plan_id = session['new_plan_id']
        
    except KeyError as ex:
        error_msg = {
            "Error: Can´t update locally the subscription because key " f"{ex.args} is missing from the request"
        }
        return HttpResponse(error_msg)
    
    else:
        del session['subscription.id']
        del session['new_plan_id']
        
    subscription = await Subscription.objects.aget(id = int(subscription_db_id))
    subscription_id = subscription.external_subscription_id
    
    
    access_token = await sub_manager.get_access_token()
    sub_details = await sub_manager.get_subscription_details(access_token, subscription_id)
    
    if not (sub_details['status'] == 'ACTIVE' and sub_details['plan_id'] == new_plan_id):
        error_msg = f'Error: Invalid subscription data during plan update'
        
        return HttpResponse(error_msg)
    
    
    new_plan_choice = await PlanChoice.objects.aget(external_plan_id = new_plan_id)
    subscription.plan_choice = new_plan_choice
    
    await subscription.asave()
    
    return await arender(request, 'client/update-subscription-confirmed.html')
   
   
@aclient_required
async def password_update_client(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user, request.POST)
        if await form.ais_valid():
            
            new_password1 = request.POST.get('new_password1')

            # Check if the old password is the same as the new one
            if check_password(new_password1, user.password):
                messages.warning(request, "Your new password must be different from your old password.")
            
            else:
                user = await form.asave()
                await alogout(request)
                return redirect('home')
        
        else:
            messages.error(request, "There was an error updating your password. Please correct the form errors.")

    else:
        form = CustomPasswordChangeForm(user)
    
    context = {
        'password_form': form,
    }
    return await arender(request, 'client/password-update.html', context)


@aclient_required
async def delete_account_client(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    
    if request.method == 'POST':
        await user.adelete()
        return redirect('home')
    
    context = {'user': user}
    return await arender(request, 'client/delete-account.html', context)
 
  