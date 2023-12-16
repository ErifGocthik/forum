from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin

from forum_profile.models import Profile


class RequireProfileMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        user = request.user
        if not user.is_authenticated:
            return None

        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return None

        return None

