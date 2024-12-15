from rest_framework.views import APIView
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User

# Create your views here.
class SignupView(APIView):
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, format=None):
        if User.objects.filter(**request.data).exists():
            user = User.objects.filter(**request.data).first()
            request.session["email"] = user.email
            message = "Login Successful"
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = "Invalid Username/Password"
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)