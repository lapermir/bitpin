from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, UserSerializer
from .models import Product


class Products(APIView):
    """
    List all products on GET
    Create a new one on POST
    """
    # permission_classes = [IsAuthenticated]

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


class ProductEdit(APIView):
    """
    Return detail of the post on GET
    Update the score on PUT
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        user = request.user
        print(user)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        score = request.data['score']
        if score in range(6):
            product.score += score
            product.save()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
