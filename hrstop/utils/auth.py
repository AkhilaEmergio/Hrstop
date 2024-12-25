from django.conf import settings
import jwt
from ninja.security import HttpBearer
from employee.models import *

class AsyncJWTAuth(HttpBearer):
    async def authenticate(self, request, token):
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')
        user = await UserProfile.objects.aget(id=user_id)
        return user
    
