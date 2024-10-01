from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    birth_date = serializers.DateField()
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','email',
                  'password','birth_date','first_name','last_name']
        
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email','first_name', 'last_name']