from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name ='client-dashboard'),
    path('browse-articles/', views.browse_articles, name ='browse-articles'),
<<<<<<< HEAD
    path('subscription-plan/', views.subscription_plan, name ='subscription-plan'),
    path('update-client/', views.update_client, name ='update-client'),
    path('delete-account-client/', views.delete_account_client, name ='delete-account-client'),
    path('password-update-client/', views.password_update_client, name ='password-update-client'),
    path('create-subscription/<str:sub_id>/<str:plan_code>', views.create_subscription, name ='create-subscription'),
    path('cancel-subscription/<int:id>', views.cancel_subscription, name ='cancel-subscription'),
    path('update-subscription/<int:id>', views.update_subscription, name ='update-subscription'),
    path('update-subscription-confirmed/', views.update_subscription_confirmed, name ='update-subscription-confirmed'),
=======
    path('subscription-plan/', views.subscribe_plan, name ='subscription-plan'),
    path('update-client/', views.update_client, name ='update-client'),
    path('create-subscription/<str:sub_id>/<str:plan_code>', views.create_subscription, name ='create-subscription'),
>>>>>>> refs/remotes/origin/main
]
