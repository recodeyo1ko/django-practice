from django.shortcuts import render, redirect
from . import forms
from .models import User

# Create your views here.

def login(request):
    # if request.session.get('is_login', None):
    #     return redirect('/')
    # if request.method == "POST":
    #       login_form = forms.UserForm(request.POST)
    #       message = "入力した内容を再度確認してください。"
    #       if login_form.is_valid():
    #           user_id = login_form.cleaned_data['id']
    #           username = login_form.cleaned_data['username']
    #           password = login_form.cleaned_data['password']
    #           try:
    #               user = User.objects.get(user_id=user_id)
    #           except:
    #               message = "ユーザーが存在しません。"
    #               return render(request, 'account/login.html', locals())

    #           if user.password == password:
    #               request.session['is_login'] = True
    #               request.session['user_id'] = user.user_id
    #               return redirect('/')
    #           else:
    #               message = "パスワードが正しくありません。"
    #               return render(request, 'account/login.html', locals())
    # else:
    #     return render(request, 'account/login.html', locals())
    # login_form = forms.UserForm()
    return render(request, 'account/login.html')

def registerUser(request):
    return render(request, 'account/registerUser.html')

def registerUserCommit(request):
    return render(request, 'account/registerUserCommit.html')

def registerUserComfirm(request):
    return render(request, 'account/registerUserComfirm.html')

def updateUser(request):
    return render(request, 'account/updateUser.html')

def updateUserCommit(request):
    return render(request, 'account/updateUserCommit.html')

def updateUserComfirm(request):
    return render(request, 'account/updateUserComfirm.html')

def userinfo(request):
    return render(request, 'account/userinfo.html')

def withdrawCommit(request):
    return render(request, 'account/withdrawCommit.html')

def withdrawComfirm(request):
    return render(request, 'account/withdrawComfirm.html')



def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    request.session.flush()
    return redirect('/')