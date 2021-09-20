from .models import Account, Booster
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import permission_classes

from .serializers import BoosterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# API
@permission_classes([AllowAny])
class BoostersList(APIView):
    def get(self, request, format=None):
        boosters = Booster.objects.all()
        serializers = BoosterSerializer(boosters, many=True, context={"request": request})
        return Response(serializers.data)
