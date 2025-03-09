from django.utils import timezone
from django.db import models
from django.utils.translation import gettext as _t2
from django.utils.translation import gettext_lazy as _t
<<<<<<< HEAD
from django.core.exceptions import ObjectDoesNotExist
=======
>>>>>>> refs/remotes/origin/main

from asgiref.sync import sync_to_async

from account.models import CustomUser

EXTERNAL_ID_MAX_LEN = 255
EXTERNAL_API_URL_MAX_LEN = 2000
EXTERNAL_STYLE_MAX_LEN = 2000

PLAN_CHOICE_NAME_MAX_LEN = 30  # Plan Name
PLAN_CHOICE_DESCRIPTION_MAX_LEN = 300 # Plan Description

SUBSCRIPTION_COST_DIGITS = 5


class PlanChoice(models.Model):
    plan_code = models.CharField(max_length=2, unique=True, blank=False, verbose_name= _t('Plan code'))
    
    name = models.CharField(max_length=PLAN_CHOICE_NAME_MAX_LEN, unique=True, blank=False, verbose_name= _t('Plan name'))
    
    cost = models.DecimalField(max_digits=SUBSCRIPTION_COST_DIGITS, decimal_places = 2, verbose_name=_t('Plan Cost'))
    
    
    is_active = models.BooleanField(default=False)
    
    
    date_added = models.DateTimeField(default= timezone.now)
    date_changed = models.DateTimeField(default= timezone.now)
    
    
    description1 = models.CharField(max_length=PLAN_CHOICE_DESCRIPTION_MAX_LEN, verbose_name= _t('Plan description 1:'))
    
    description2 = models.CharField(max_length=PLAN_CHOICE_DESCRIPTION_MAX_LEN, verbose_name= _t('Plan description 2:'))
    
    
    external_plan_id = models.CharField(max_length=EXTERNAL_ID_MAX_LEN, unique=True, verbose_name= _t('External plan id'))
    
    external_api_url = models.CharField(max_length=EXTERNAL_API_URL_MAX_LEN, unique=True, verbose_name= _t('External API URL'))
    
    external_style_json = models.CharField(max_length=EXTERNAL_STYLE_MAX_LEN, verbose_name= _t('External Style (json)'))
    
    
    
    
    def __str__(self) -> str:
<<<<<<< HEAD
        return f'{str(self.name)} subscription'
=======
        return f'{str("self.name")} subscription'
>>>>>>> refs/remotes/origin/main
    
    @classmethod
    def from_plan_code(cls, plan_code:str) -> 'PlanChoice':
        return PlanChoice.objects.get(plan_code = plan_code)
    
    
    @classmethod
    async def afrom_plan_code(cls, plan_code:str) -> 'PlanChoice':
        return await PlanChoice.objects.aget(plan_code = plan_code)
#:



class Subscription(models.Model):
    
    cost = models.DecimalField(max_digits=SUBSCRIPTION_COST_DIGITS, decimal_places = 2, verbose_name=_t('Subscription Cost'))
    
    external_subscription_id = models.CharField(
        max_length= EXTERNAL_ID_MAX_LEN, verbose_name= _t('External subscription ID')
    )
    
    
    is_active = models.BooleanField(default=False)
    
    
    date_added = models.DateTimeField(default= timezone.now)
    
    
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    
    plan_choice = models.ForeignKey(PlanChoice, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
<<<<<<< HEAD
        plan_choice = self.plan_choice
=======
        plan_choice = Subscription.PlanChoices(self.plan_choice)
>>>>>>> refs/remotes/origin/main
        return f'{self.user.first_name} {self.user.last_name}: {plan_choice.name} {_t2("subscription")}'
    
    
    
    async def aplan_choice(self) -> PlanChoice:
        
        @sync_to_async
        def call_sync_fk() -> PlanChoice:
            return self.plan_choice
        
<<<<<<< HEAD
        return await call_sync_fk()
        
        
    async def ais_premium(self) -> bool:
        return (await self.aplan_choice()).plan_code == 'PR'
    
    
    @staticmethod
    async def afor_user(user: CustomUser,status = '') -> 'Subscription|None':
        kargs: dict = {'user': user}
        if status in ('A', 'I'):
            kargs.update(is_active = (status == 'A'))
            
        try:
            return await Subscription.objects.aget(**kargs)
        
        except ObjectDoesNotExist:
            return None
=======
        
    async def ais_premium(self) -> bool:
        (await self.aplan_choice()).plan_code == 'PR'
        
>>>>>>> refs/remotes/origin/main
