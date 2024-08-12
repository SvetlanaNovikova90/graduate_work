from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
import random
import secrets
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserRegisterForm, PasswordRecoveryForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('clinic:index')


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/user_form.html"
    fields = ('email', 'password1', 'password2',)
    success_url = reverse_lazy('users:login')


class RegisterMessageView(TemplateView):
    template_name = 'users/register_message.html'

#
# class PasswordRecoveryMessageView(TemplateView):
#     template_name = 'users/password_recovery_message.html'
#
#
# @csrf_exempt
# def email_verification(request, token):
#     user = get_object_or_404(User, token=token)
#     user.is_active = True
#     return HttpResponseRedirect('/users/login/')
#
#
# class PasswordRecoveryView(TemplateView):
#     model = User
#     template_name = 'users/password_recovery_form.html'
#     form_class = PasswordRecoveryForm
#     success_url = reverse_lazy('users:recovery_message')
#
#     code = secrets.token_hex(8)
#
#     def post(self, request, *args, **kwargs):
#         email = request.POST.get('email')
#         user = User.objects.get(email=email)
#         code = PasswordRecoveryView.code
#         user.set_password(PasswordRecoveryView.code)
#         user.save()
#
#         host = self.request.get_host()
#         url = f'http://{host}/users/login/'
#
#         send_mail(
#             'Восстановление пароля',
#             f'Ваш новый пароль {code}, перейдите по ссылке {url}',
#             EMAIL_HOST_USER,
#             [user.email],
#         )
#         return HttpResponseRedirect('/users/password_recovery/message/')
