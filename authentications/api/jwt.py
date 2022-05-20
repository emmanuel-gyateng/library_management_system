from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
import jwt
from django.conf import settings
from ..models import Users


class JWTBaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_hearder = get_authorization_header(request)
        auth_data = auth_hearder.decode('utf-8')
        auth_token = auth_data.split(" ")
        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed("Token not valid")
        token = auth_token[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            username = payload["username"]
            user = Users.objects.get(username=username)
            return (user, token)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token Expired, login again")

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Token is invalid")
        
        except Users.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
