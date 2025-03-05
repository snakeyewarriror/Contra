from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import aget_user
from common.auth import aclient_required
from common.django_utils import arender

from .models import Subscription, PlanChoice
from writer.models import Article

@aclient_required
async def dashboard(resquest: HttpRequest) -> HttpResponse:
    
    user = await aget_user(resquest)
    
    try:
        
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        plan = (await subscription.aplan_choice()).name
        subscription_plan = plan.name
    
    except ObjectDoesNotExist:
        subscription_plan = 'no subscription yet'
    
    
    
    context = {'subscription_plan': subscription_plan}
    return await arender(resquest, 'client/dashboard.html', context)


@aclient_required
async def browse_articles(resquest: HttpRequest) -> HttpResponse:
    
    user = await aget_user(resquest)
    
    try:
        
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        
        if not await subscription.ais_premium():
            articles = Article.objects.filter(is_premium = False)
            
        else:
            articles =Article.objects.all()
    
    except ObjectDoesNotExist:
        has_subscription = False
        articles = []
    

    context = {'has_subscription': has_subscription, 'articles': articles}
    return await arender(resquest, 'client/browse-articles.html', context)



@aclient_required
async def subscribe_plan(resquest: HttpRequest) -> HttpResponse:
    
    context = { "plan_choices": PlanChoice.objects.filter(is_active = True) }
    
    
    return await arender(resquest, 'client/subscription-plan.html', context)



@aclient_required
async def update_client(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    subscription = None
    
    
    try:
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        
    except ObjectDoesNotExist:
        pass
    
    context = {"has_subscription": subscription is not None}
    return await arender(request, 'client/update-client.html', context)


@aclient_required
async def create_subscription(request: HttpRequest, sub_id: str, plan_code: str) -> HttpResponse:
    
    plan_choice = await PlanChoice.afrom_plan_code(plan_code)
    user = await aget_user(request)
    
    await Subscription.objects.acreate(
        plan_choice = plan_choice,
        cost = plan_choice.cost,
        external_subscription_id = sub_id,
        is_active = True,
        user = user,
    )
    
    
    context = {'subscription_plan': plan_choice.name}
    return await arender(request, 'client/create-subscription.html', context)
