from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import UserLoginSerializer, UserModelSerializer, UserSignupSerializer
from users.models import User

# # Create your views here.
class UsersViewSet(viewsets.GenericViewSet):
    
    query_set= User.objects.all()
    serializer_class= UserModelSerializer


    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serialized = UserSignupSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user=serialized.save()
        data = UserModelSerializer(user).data
       
        return Response(data, status=status.HTTP_201_CREATED)
    