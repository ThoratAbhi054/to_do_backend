from iam.user.models import UserProfile
from utils.mixins.cms_mixin import StatusChoices


class ProfileCreationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            if not UserProfile.objects.filter(user=request.user).exists():
                UserProfile.objects.create(
                    user=request.user, status=StatusChoices.PUBLISHED
                )
        return response
