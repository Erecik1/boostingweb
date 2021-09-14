from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Order
from django.http import Http404
from lolboost.models import Order
from lolboost.serializers import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializers = OrderSerializer(orders, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404