from rest_framework import serializers

from .models import Account, Booster

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "username",
        )


class BoosterSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='account.username')
    profile_image = serializers.ReadOnlyField(source='account.get_image')

    class Meta:
        model = Booster
        fields = (
            "username",
            "about",
            "rank",
            "reviews",
            "reviews_rate",
            "regions",
            "orders_done",
            "languages",
            "profile_image",
        )
