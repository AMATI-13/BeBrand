from django.urls import path
from .views import home, user_info

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('user/<int:user_id>/', user_info, name='user_info'),
]