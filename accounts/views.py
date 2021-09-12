from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationsForm

from .serializers import AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

def indexView(request):
    return render(request,'index.html')
@login_required()

def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = RegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')

    else:
        form = RegistrationsForm()
    return render(request,'registration/register.html',{'form':form})


#API
class BoostersList(APIView):
    def get(self, request, format=None):
        boosters = Account.objects.filter(is_booster=True)
        serializers = AccountSerializer(boosters, many=True)
        return Response(serializers.data)
