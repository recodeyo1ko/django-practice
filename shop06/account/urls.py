from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),

    path('registerUser/', views.RegisterUserView.as_view(), name='registerUser'),
    path('registerUserCommit/', views.registerUserCommit, name='registerUserCommit'),
    path('updateUser/', views.updateUser, name='updateUser'),
    path('updateUserCommit/', views.updateUserCommit, name='updateUserCommit'),
    path('updateUserComfirm/', views.updateUserComfirm, name='updateUserComfirm'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('withdrawCommit/', views.withdrawCommit, name='withdrawCommit'),
    path('withdrawComfirm/', views.withdrawComfirm, name='withdrawComfirm'),
]