from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import CustomLogoutView, UserCreateView, email_verification

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='/'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_verification'),
]
