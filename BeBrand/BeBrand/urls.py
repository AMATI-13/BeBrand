from django.contrib import admin
from django.urls import path, include
from main.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('', home, name = 'home'),  # Этот маршрут обрабатывать пустой URL
]