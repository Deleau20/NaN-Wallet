from django.urls import path
from .views import register, login, logOut, forgot_pwd


urlpatterns = [
    path('register', register, name='register'),
    path('login/', login, name='login'),
    path('logout', logOut, name='logout'),
    path('password_reset', forgot_pwd, name='password_reset'),
]