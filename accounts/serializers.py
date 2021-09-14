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
    profile_url = serializers.SerializerMethodField()

    class Meta:
        model = Booster
        fields = "__all__"

    def get_profile_url(self, booster):
        photo_url = booster.account.profile_image.url
        return "127.0.0.1:8000" + photo_url