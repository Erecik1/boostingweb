from .models import Account, Booster
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationsForm

from .serializers import BoosterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


def indexView(request):
    return render(request, 'index.html')


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
    return render(request, 'registration/register.html', {'form': form})


# API
class BoostersList(APIView):
    def get(self, request, format=None):
        boosters = Booster.objects.all()
        serializers = BoosterSerializer(boosters, many=True, context={"request": request})
        return Response(serializers.data)
