from django.urls import path
from . import views

urlpatterns = [
    # path('', views.chatbot, name='chatbot'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    # this side is my urls i am abdullah khan
    path('', views.chatpage, name='chatbot'),
    path('logins/', views.log, name='log'),
    path('registers/', views.reg, name='reg'),
    path('chatpage/', views.chatpage, name='chatpage'),

    


    
]