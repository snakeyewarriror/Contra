from django import forms
from django.forms import Form, ModelForm
from common.django_utils import AsyncModelFormMixin
from django.utils.translation import gettext_lazy as _t

from typing import Iterable
from asgiref.sync import sync_to_async
from .models import PlanChoice
from account.models import CustomUser

class UpdateSubscriptionForm(Form, AsyncModelFormMixin):
    plan_choices = forms.ChoiceField(
        label=_t('Update Plan Choices'),
    )
        
    def __init__(self, *args, exclude: Iterable[str] | None = None, format_fn = lambda plan_choice: plan_choice.name, **kwargs):
        super().__init__(*args, **kwargs)
        plan_choices = PlanChoice.objects.filter(is_active = True)
        
        if exclude:
            plan_choices = plan_choices.exclude(plan_code__in = exclude)
            
        self.fields['plan_choices'].choices = ((
            plan_choice.plan_code, format_fn(plan_choice)) for plan_choice in plan_choices
        )
        
        
    @classmethod
    def ainit(cls, *args, **kwargs):
        
        @sync_to_async
        def call_init() -> UpdateSubscriptionForm:
            return UpdateSubscriptionForm(*args, **kwargs)
        
        return call_init()
   
    
class UpdateUserForm(ModelForm, AsyncModelFormMixin):
    class Meta:
        model = CustomUser
        fields = {
            'email',
            'first_name',
            'last_name'
        }


