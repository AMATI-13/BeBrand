from django.urls import path
from .views import user_info

urlpatterns = [
    path('user/<int:user_id>/', user_info, name='user_info'),
]