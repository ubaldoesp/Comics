from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator,FileExtensionValidator

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','name','email','password')
        
class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)
    # validar datos 
    def validate(self,data):
        # autenticar recibe las credenciales, si son validas
        print(data)
        user = authenticate(username=data['email'], password=data['password'])
        print(user)
        if not user:
            raise serializers.ValidationError('Las credenciales no son validas')
        
        self.context['user'] = user
        return data
    
    def create(self, data):
        """Generar Token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
    
class UserSignupSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
    validators=[UniqueValidator(queryset=User.objects.all())]
            
    )
    username = serializers.CharField(
    min_length=4,
    max_length=20,
    validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    name= serializers.CharField(
        min_length=4,
        max_length=20,
    )
    
    age= serializers.IntegerField()
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        
        passwd = data['password']
        
        passwd_conf = data['password_confirmation']
        
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        
        password_validation.validate_password(passwd)
        
        return data
        # print(pas_val)
    def create(self, data):
        data.pop('password_confirmation')
        print(data)
        user = User.objects.create(**data)
        return user