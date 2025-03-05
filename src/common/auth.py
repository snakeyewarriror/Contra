from functools import wraps

from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import aget_user
from django.shortcuts import redirect

from common.django_utils import AsyncViewT




def aclient_required(client_view: AsyncViewT):
    
    @wraps(client_view)
    @login_required(login_url = 'login')
    async def function(resquest: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = await aget_user(resquest)
        
        if user.is_authenticated and not user.is_writter:
            return await client_view(resquest, *args, **kwargs)
        
        return HttpResponseForbidden("Only clients can acess this view.")
    
    return function


def awriter_required(writer_view: AsyncViewT):
    @wraps(writer_view)
    @login_required(login_url = 'login')
    async def function(resquest: HttpRequest, *args, **kwargs) -> HttpResponse:
        user = await aget_user(resquest)
        
        if user.is_authenticated and user.is_writter:
            return await writer_view(resquest, *args, **kwargs)
        
        return HttpResponseForbidden("Only writers can acess this view.")
    
    return function



def ensure_for_current_user(model: type, *, id_in_url: str = 'id', redirect_if_missing: str):
    def decorator(view: AsyncViewT):
        async def async_view(request: HttpRequest, *args, **kargs) -> HttpResponse:
            obj_id = kargs[id_in_url]
            current_user = await aget_user(request)
            
            try:
                obj = await model.objects.aget(id = obj_id, user = current_user)
                del kargs[id_in_url]
                return await view(request, obj, *args, **kargs)
            except ObjectDoesNotExist:
                return redirect(redirect_if_missing)
            
        return async_view
    return decorator

