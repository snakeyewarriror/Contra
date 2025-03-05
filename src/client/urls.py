from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name ='client-dashboard'),
    path('browse-articles/', views.browse_articles, name ='browse-articles'),
    path('subscription-plan/', views.subscribe_plan, name ='subscription-plan'),
    path('update-client/', views.update_client, name ='update-client'),
    path('create-subscription/<str:sub_id>/<str:plan_code>', views.create_subscription, name ='create-subscription'),
]
