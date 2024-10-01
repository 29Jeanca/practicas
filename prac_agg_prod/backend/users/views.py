from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import RegisterAllUsersSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Register

# Create your views here.
class RegisterAccount(APIView):
    def post(self,request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if Register.objects.filter(email=email).exists():
            return Response({'message':'Email already exists'})
        
        if name and email and password:
            Register.objects.create(name=name,email=email,password=password)
            return Response({'success':'Account created successfully'},status=201)
        else:
            return Response({'error':'Invalid data'})
        
class LoginAccount(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
       
        if Register.objects.filter(email=email,password=password).exists():
            return Response({'success':'Login successful'},status=200)
        else:
            return Response({'error':'Invalid credentials'})
        
# class LoginAccount(APIView):
#     def post(self,request):
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         if Register.objects.filter(email=email,password=password).exists():
#             refresh = RefreshToken.for_user(Register.objects.get(email=email))
#             return Response({'success':'Login successful','refresh':str(refresh),'access':str(refresh.access_token)})

#         else:
#             return Response({'error':'Invalid credentials'})
        

class GetAllUsers(ListAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterAllUsersSerializer