from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerUserCommit/', views.registerUserCommit, name='registerUserCommit'),
    path('registerUserComfirm/', views.registerUserComfirm, name='registerUserComfirm'),
    path('updateUser/', views.updateUser, name='updateUser'),
    path('updateUserCommit/', views.updateUserCommit, name='updateUserCommit'),
    path('updateUserComfirm/', views.updateUserComfirm, name='updateUserComfirm'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('withdrawCommit/', views.withdrawCommit, name='withdrawCommit'),
    path('withdrawComfirm/', views.withdrawComfirm, name='withdrawComfirm'),
]