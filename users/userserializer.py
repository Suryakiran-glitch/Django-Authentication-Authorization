from rest_framework import serializers
from .models import Usermodel

class Userserializer(serializers.ModelSerializer):
 class Meta:
  model=Usermodel
  fields = "__all__"
  extra_kwargs = {
   'password': {'write_only': True}
  }