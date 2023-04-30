from django.urls import path
from .views import protected_view

app_name = 'api_auth'

urlpatterns = [
    path('protected/', protected_view, name='protected')
]