from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'role')
    search_fields = ('user__username',)
 #Пароль(root): 1234, Почта: root@mail.ru
admin.site.register(UserProfile, UserProfileAdmin)