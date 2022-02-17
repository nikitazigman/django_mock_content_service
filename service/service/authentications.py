from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication
from rest_framework_simplejwt.backends import TokenBackend


class CustomAnonymousUser(AnonymousUser):
    """
    Always return True. This is a way to tell if
    the user has been authenticated in permissions
    """

    @property
    def is_authenticated(self):
        return True


class JWTThirdPartyAuthentication(authentication.BaseAuthentication):
    """
    Custom Jwt auth class, the token verification is done on API Gateway,
    which placed above the service so the class just retrieve
    the payload part of the token to use UserID
    """

    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION", " ").split(" ")[1]
        valid_data = TokenBackend(algorithm="HS256").decode(token, verify=False)

        user = CustomAnonymousUser()
        user.user_id = valid_data["user_id"]

        return user, token
