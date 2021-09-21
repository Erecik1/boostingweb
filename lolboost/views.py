from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from accounts.models import Account
from .models import Order
from django.http import Http404
from lolboost.models import Order
from lolboost.serializers import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import permission_classes
from lolboost.permissions import BoostersReadOnly

def calculateBoostPrice(data):
    print(data)
    return 100

class OrderList(APIView):
    @permission_classes([BoostersReadOnly])
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializers = OrderSerializer(orders, many=True)
        return Response(serializers.data)
    @permission_classes([IsAuthenticated])
    def post(self, request, format=None):
        user = request.user.id
        request.data["user"] = user
        request.data["price"] = calculateBoostPrice(request.data)
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([BoostersReadOnly])
class OrderDetail(APIView):
    def get(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404