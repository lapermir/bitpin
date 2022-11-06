from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product


class Products(APIView):
    """
    List all products, or create a new one
    """

    def get(self, request):
        product = get_list_or_404(Product)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
