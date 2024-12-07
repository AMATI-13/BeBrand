from django.http import JsonResponse
from .models import UserProfile

def user_info(request, user_id):
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        data = {
            'username': profile.user.username,
            'balance': str(profile.balance),
            'role': profile.role,
        }
        return JsonResponse(data)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)