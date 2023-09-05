from django.urls import path
from .views import show_dash


urlpatterns = [
    path('dash/', show_dash, name='dash_client'),
]