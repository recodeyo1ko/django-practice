from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),

    path('registerUser/', views.RegisterUserView.as_view(), name='registerUser'),
    path('registerUserCommit/', views.registerUserCommit, name='registerUserCommit'),

    path('userInfo/', views.userInfo, name='userInfo'),
    path('updateUser/', views.UpdateUserView.as_view(), name='updateUser'),
    path('updateUserCommit/', views.updateUserCommit, name='updateUserCommit'),

    path('withdrawCommit/', views.withdrawCommit, name='withdrawCommit'),
    path('withdrawComfirm/', views.withdrawComfirm, name='withdrawComfirm'),
]