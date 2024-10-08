from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, activate, email_activate, restore_password, VerifyEmailView, \
    UserDetailView, RecordingCreateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('activate/<str:uid>/', activate, name="activate"),
    path('email_activated/', email_activate, name="email_activated"),
    path('restore_password/', restore_password, name="restore_password"),
    path('verify_email/<int:pk>/', VerifyEmailView.as_view(), name='verify_email'),
    path("user/<int:pk>/", UserDetailView.as_view(), name='user_detail'),
    # path("user/<int:pk>/update/", UserUpdateView.as_view(), name='user_update'),
    path("recording/create/", RecordingCreateView.as_view(), name='recording_create'),
]
