from rest_framework import serializers

from .models import Account, Booster
import os

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "username",
        )


class BoosterSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='account.username')
    profile_image = serializers.ReadOnlyField(source='account.profile_image.url')

    class Meta:
        model = Booster
        fields = "__all__"