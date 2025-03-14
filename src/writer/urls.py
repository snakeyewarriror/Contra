from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name ='writer-dashboard'),
    path('my-articles/', views.my_articles, name ='my-articles'),
    path('create-article/', views.create_article, name ='create-article'),
    path('update-article/<int:id>', views.update_article, name ='update-article'),
    path('delete-article/<int:id>', views.delete_article, name ='delete-article'),
    path('update-writer/', views.update_writer, name ='update-writer'),
    path('delete-account/', views.delete_account, name ='delete-account'),
    path('password-update/', views.password_update, name ='password-update'),
]
