from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _t

from account.models import CustomUser

TITLE_MAXLEN = 100
CONTENT_MAXLEN = 3000


class Article(models.Model):
    title = models.CharField(max_length=TITLE_MAXLEN, verbose_name= _t('Title'))
    content = models.TextField(max_length=CONTENT_MAXLEN, verbose_name= _t('Content'))
    date_poster = models.DateTimeField(default= timezone.now)
    is_premium = models.BooleanField(default= False, verbose_name= _t('Is this a premium article?'))
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    