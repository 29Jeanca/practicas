from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class AllProductsView(generics.ListCreateAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

# class AddProduct(APIView):
#     parser_classes = [IsAuthenticated]
#     def post(self,request):
#         name = request.data.get('name')
#         price = request.data.get('price')
#         description = request.data.get('description')
#         image = request.data.get('image')

#         if not request.user.is_authenticated:
#             return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

#         if not all([name, price, description, image]):
#             return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
#         Product.objects.create(
#             id_user=request.user,
#             name=name,
#             price=price,
#             description=description,
#             image=image,
#         )
#         return Response({'success': 'Product created'}, status=status.HTTP_201_CREATED)


        


