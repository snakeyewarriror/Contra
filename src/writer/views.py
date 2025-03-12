from django.http import HttpRequest, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import aget_user
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages

from common.auth import ensure_for_current_user
from common.django_utils import arender, alogout
from common.auth import awriter_required
from writer.forms import ArticleForm, UpdateUserForm
from .models import Article
from common.forms import CustomPasswordChangeForm

@awriter_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    
    """
    This is the writer dashboard
    
    """
    
    return await arender(request, 'writer/dashboard.html')


@awriter_required
async def create_article(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if await form.ais_valid():
            article = await form.asave(commit = False)
            article.user = await aget_user(request)
            await article.asave()
            return redirect("my-articles")
        
    else:
        form = ArticleForm()
            
            
    context = {'create_article_form': form}
    return await arender(request, 'writer/create-article.html', context)


@awriter_required
async def my_articles(request: HttpRequest) -> HttpResponse:
    
    user = await aget_user(request)
    articles = Article.objects.filter(user = user)
    context = {"my_articles": articles}
    
    return await arender(request, 'writer/my-articles.html', context)


@awriter_required
@ensure_for_current_user(Article, redirect_if_missing='my-articles')
async def update_article(request: HttpRequest, article: Article) -> HttpResponse:
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article)
        
        if await form.ais_valid():
            article = await form.asave(commit = False)
            article.user = await aget_user(request)
            await article.asave()
            return redirect("my-articles")
        
    else:
        form = ArticleForm(instance = article)
            
            
    context = {'update_article_form': form}
    return await arender(request, 'writer/update-article.html', context)


@awriter_required
@ensure_for_current_user(Article, redirect_if_missing='my-articles')
async def delete_article(request: HttpRequest, article: Article) -> HttpResponse:
    if request.method == 'POST':
        
        await article.adelete()
        return redirect("my-articles")
            
    context = {'article': article}
    return await arender(request, 'writer/delete-article.html', context)


@awriter_required
async def update_writer(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance= user)
        
        if await form.ais_valid():
            await form.asave()
            return redirect('writer-dashboard')
        
    else:
        form = UpdateUserForm(instance= user)
        
    context = {'update_user_form': form}
    return await arender(request, 'writer/update-writer.html', context)
        

@awriter_required
async def delete_account(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    
    if request.method == 'POST':
        await user.adelete()
        return redirect('home')
    
    context = {'user': user}
    return await arender(request, 'writer/delete-account.html', context)


@awriter_required
async def password_update(request: HttpRequest) -> HttpResponse:
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
    return await arender(request, 'writer/password-update.html', context)
