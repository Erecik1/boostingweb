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
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from lolboost.permissions import BoostersReadOnly

price_tab = [
    0,
    17,
    17,
    17,
    31,
    17,
    17,
    17,
    31,
    17,
    17,
    17,
    31,
    19,
    19,
    19,
    33,
    26,
    29,
    31,
    52,
    68,
    82,
    116,
    217,]

rankData = [
    "Iron Division 4",
    "Iron Division 3",
    "Iron Division 2",
    "Iron Division 1",
    "Bronze Division 4",
    "Bronze Division 3",
    "Bronze Division 2",
    "Bronze Division 1",
    "Silver Division 4",
    "Silver Division 3",
    "Silver Division 2",
    "Silver Division 1",
    "Gold Division 4",
    "Gold Division 3",
    "Gold Division 2",
    "Gold Division 1",
    "Platinum Division 4",
    "Platinum Division 3",
    "Platinum Division 2",
    "Platinum Division 1",
    "Diamond Division 4",
    "Diamond Division 3",
    "Diamond Division 2",
    "Diamond Division 1",
    "Master",
]
def leaguesToPrice(leagues):
    price = 0
    for league in leagues:
        price += price_tab[league-1]
    return price

def calculateBoostPrice(data):
    multi = 1
    starting_league = data['league_from'] + " " + data['division_from']
    if data['league_to'] == 'Master':
        target_league = data['league_to']
    else:
        target_league = data['league_to'] + " " + data['division_to']
    count = False
    leagues = []
    key = 0
    for rank in rankData:
        key += 1
        if count:
            leagues.append(key)
        if starting_league == rank:
            count = True
        if target_league == rank:
            break
    price = leaguesToPrice(leagues)
    if data['is_duo']:
        multi *= 1.35
    if data['is_high_priority']:
        multi *= 1.2
    if data['isStream']:
        multi * 1.1

    if data['lp_gain'] == "1-9":
        multi *= 1.3
    elif data['lp_gain'] == "10-14":
        multi *= 1.15
    elif data['lp_gain'] == "15-18":
        multi *= 1
    elif data['lp_gain'] == "19-24":
        multi *= 0.9
    elif data['lp_gain'] == "25+":
        multi *= 0.75
    price *= multi
    price = round(price, 2)
    return price

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
