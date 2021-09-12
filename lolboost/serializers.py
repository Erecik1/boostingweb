from rest_framework import serializers

from lolboost.models import DivisionBoosting

class DivisionBoostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionBoosting
        fields = (
            "order_id",
            "queue",
            "start_rank",
            "start_div",
            "start_lp",
            "gain_lp",
            "end_rank",
            "end_div",
        )