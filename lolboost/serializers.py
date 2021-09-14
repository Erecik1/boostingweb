from rest_framework import serializers

from lolboost.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "status",
            "boosting_type",
            "time_created",
            "booster",
            "order_price",
            "account_region",
            "discount",
            "is_duo",
            "is_flex",
            "is_high_priority",
            "is_role_champion",
            "is_stream",
            "promo_code",
            "wins_to_play",
            "division_from",
            "division_to",
            "league_from",
            "league_to",
            "lp_from",
            "lp_gain",
        )
