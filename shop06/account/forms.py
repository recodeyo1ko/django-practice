from django import forms
from .models import User


class UserLoginForm(forms.Form):
    user_id = forms.IntegerField(label='ユーザーID')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    
    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not user_id:
            raise forms.ValidationError('ユーザーIDを入力してください')
        return user_id
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('パスワードを入力してください')
        return password


# class UserRegistrationForm(forms.Form):
#     user_id = forms.IntegerField(label='ユーザーID')
#     username = forms.CharField(label='ユーザー名')
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
#     address = forms.CharField(label='住所')

#     def clean_user_id(self):
#         user_id = self.cleaned_data['user_id']
#         if user_id == '':
#             raise forms.ValidationError('ユーザーIDを入力してください')
#         if User.objects.filter(user_id=user_id).exists():
#             raise forms.ValidationError('このユーザーIDはすでに登録されています')
#         return user_id
    
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if username == '':
#             raise forms.ValidationError('ユーザー名を入力してください')
#         return username
    
#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if password == '':
#             raise forms.ValidationError('パスワードを入力してください')
#         return password
    
#     def clean_address(self):
#         address = self.cleaned_data['address']
#         if address == '':
#             raise forms.ValidationError('住所を入力してください')
#         return address