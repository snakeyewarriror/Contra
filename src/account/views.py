from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import django.contrib.auth as auth
<<<<<<< HEAD
from common.django_utils import arender, alogout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from common.auth import aanonymous_required


@aanonymous_required
async def home(request: HttpRequest) -> HttpResponse:
    return await arender(request, 'account/home.html')


@aanonymous_required
=======


from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from common.django_utils import arender, alogout

async def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/home.html')


>>>>>>> refs/remotes/origin/main
async def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if await form.ais_valid():
            await form.asave()
            return redirect('login')
        
        
    else:
        form = CustomUserCreationForm()
        
    
    context = {'register_form': form}
    return await arender(request, 'account/register.html', context)


<<<<<<< HEAD
@aanonymous_required
=======
>>>>>>> refs/remotes/origin/main
async def login(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data = request.POST)
        if await form.ais_valid():
            email = request.POST['username']
            passwd = request.POST['password']
            user: CustomUser | None = await auth.aauthenticate(
                request,
                username = email,
                password = passwd,
            )
            
            if user:
                await auth.alogin(request, user)
                return redirect('writer-dashboard' if user.is_writter else 'client-dashboard')
        
    else:
        form = CustomAuthenticationForm()
        
    
    context = {'login_form': form}
    return await arender(request, 'account/login.html', context)


<<<<<<< HEAD
@login_required(login_url='login')
async def logout(request: HttpRequest) -> HttpResponse:
    await alogout(request)
    return redirect('/')
=======
async def logout(request: HttpRequest) -> HttpResponse:
    await alogout(request)
    return redirect('/')



>>>>>>> refs/remotes/origin/main
