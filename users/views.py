from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .userserializer import Userserializer
from .models import Usermodel
from rest_framework.exceptions import APIException,AuthenticationFailed
from .authentication import generate_token,check_token
import bcrypt
import json

@api_view(['GET'])
def users(request):
 serializer = Userserializer(Usermodel.objects.all(),many=True)
 return Response(serializer.data)

@api_view(['POST'])
def register(request):
 data = request.data
 if data['password'] != data['re_password']:
  raise APIException('Passwords does not match!!!')

 hashed_password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt()).decode('utf8')
 Usermodel.objects.create(
  first_name=data['first_name'],
  last_name=data['last_name'],
  email=data['email'],
  password=hashed_password
 )
 return Response("User created",status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
 email = request.data['email']
 password = request.data['password']

 user = Usermodel.objects.filter(email=email).first()

 hash_pasword = Usermodel.objects.get(email=email).password
 check_password = bcrypt.checkpw(password.encode('utf8'),hash_pasword.encode('utf8'))

 if not user:
  raise AuthenticationFailed('User does not Exist!!!')

 response = Response()
 token = generate_token(user)
 response.set_cookie(key="jwt",value=token,httponly=True)
 response.data = {
  'token' : token,
 }

 return response

@api_view(['POST'])
def logout(request):
 check_token(request)
 response = Response()
 response.delete_cookie(key='jwt')
 response.data = {
  'message' : "Logout successfully"
 }

 return response










