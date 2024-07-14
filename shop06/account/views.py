from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .models import User

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        if request.session.get('is_login', None):
            return redirect('shopping:index')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            if User.objects.filter(user_id=user_id, password=password).exists():
                request.session['is_login'] = True
                request.session['user_id'] = user_id
                return redirect('shopping:index')
            else:
                return render(request, self.template_name, {'form': form, 'error': 'ユーザーIDまたはパスワードが間違っています'})
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form, 'error': 'フォームにエラーがあります'})

def logout(request):
    request.session.flush()
    return redirect('account:login')

class RegisterUserView(View):
    form_class = UserRegisterForm
    template_name = 'account/registerUser.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if request.method == 'POST':
                context = {
                    'user_id': request.POST.get('user_id'),
                    'name': request.POST.get('name'),
                    'password': request.POST.get('password'),
                    'address': request.POST.get('address'),
                }
            return render(request, 'account/registerUserConfirm.html', {'form': form, 'context': context})
        return render(request, self.template_name, {'form': form})

def registerUserCommit(request):
    if request.method == 'POST':
        user = User()
        user.user_id = request.POST.get('user_id')
        user.name = request.POST.get('name')
        user.password = request.POST.get('password')
        user.address = request.POST.get('address')
        user.save()
        request.session['is_login'] = True
        request.session['user_id'] =  user.user_id
        return render(request, 'account/registerUserCommit.html', {'user': user})
    else:
        form = UserRegisterForm()
        return render(request, 'account/registerUserConfirm.html', {'form': form})

def userInfo(request):
    if not request.session.get('is_login'):
        return redirect('account:login')
    user = User.objects.get(user_id=request.session.get('user_id'))
    return render(request, 'account/userInfo.html', {'user': user})

class UpdateUserView(View):
    form_class = UserUpdateForm
    template_name = 'account/updateUser.html'

    def get(self, request):
        if not request.session.get('is_login'):
            return redirect('account:login')
        user = User.objects.get(user_id=request.session.get('user_id'))
        form = self.form_class(initial={
            'user_id': user.user_id,
            'name': user.name,
            'password': user.password,
            'address': user.address
        })
        context = {
            'form': form,
            'user': user
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if request.method == 'POST':
                context = {
                    'user_id': request.POST.get('user_id'),
                    'name': request.POST.get('name'),
                    'password': request.POST.get('password'),
                    'address': request.POST.get('address'),
                }
            return render(request, 'account/updateUserConfirm.html', {'form': form, 'context': context})
        return render(request, self.template_name, {'form': form})

def updateUserCommit(request):
    if request.method == 'POST':
        user = User.objects.get(user_id=request.session.get('user_id'))
        user.name = request.POST.get('name')
        user.password = request.POST.get('password')
        user.address = request.POST.get('address')
        user.save()
        return render(request, 'account/updateUserCommit.html', {'user': user})
    else:
        form = UserUpdateForm()
        return render(request, 'account/updateUserConfirm.html', {'form': form})

def withdrawCommit(request):
    return render(request, 'account/withdrawCommit.html')

def withdrawComfirm(request):
    return render(request, 'account/withdrawComfirm.html')


