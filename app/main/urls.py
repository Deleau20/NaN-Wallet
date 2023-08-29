from django.urls import path
from .views import home, apropos, service, client, contact


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('apropos/', apropos, name='apropos'),
    path('service/', service, name='service'),
    path('client/', client, name='page-client'),
    path('contact/', contact, name='contact'),
]