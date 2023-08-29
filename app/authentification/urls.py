from django.urls import path
from .views import register, login, logOut


urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logOut, name='logout'),

]