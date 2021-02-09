import jwt
from django.conf import settings
import datetime
from rest_framework.response import Response
from .models import Usermodel
from rest_framework.exceptions import PermissionDenied

def generate_token(user):
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def check_token(request):
    token = request.headers['Authorization']
    if not token:
        Response("Token is not sent")

    try:
     payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
     id = payload['id']
     user = Usermodel.objects.filter(id=id)
     return user

    except:
        raise jwt.exceptions.ExpiredSignatureError()


def check_admin(request):
    role = request.body['role']
    if role != "admin":
        raise PermissionDenied("Can not access admin route")



