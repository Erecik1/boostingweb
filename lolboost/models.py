from accounts.models import Account, Booster
from django.db import models

RANKS = (
    ("Iron", "Iron"),
    ("Bronze", "Bronze"),
    ("Silver", "Silver"),
    ("Gold", "Gold"),
    ("Platinum", "Platinum"),
    ("Diamond", "Diamond"),
    ("Master", "Master"),
)
BOOSTING_TYPE = (
    ("1", "DIVISION"),
    ("2", "WINS"),
    ("3", "PLACEMENT"),
)
BOOSTER_RANK = (
    ("C","CHALLENGER"),
    ("GM","GRANDMASTER"),
    ("M","MASTER"),
)

DIV = (
    ("Division 1", "Division 1"),
    ("Division 2", "Division 2"),
    ("Division 3", "Division 3"),
    ("Division 4", "Division 4"),
)
REGIONS = (
    ("EUNE", "EUNE"),
    ("EUW", "EUW"),
    ("NA", "NA"),
    ("RU", "RU"),
    ("TR", "TR"),
)
QUEUE = (
    ("1", "SOLOQ"),
    ("2", "FLEXQ"),
)
FLASH_KEY = (
    ("D", "D"),
    ("F", "F"),
)
STATUS = (
    ("PENDING", "PENDING"),
    ("OPEN", "OPEN"),
    ("DONE", "DONE")
)


class Order(models.Model):
    user = models.ForeignKey(Account, null=False, on_delete=models.SET("DELETED"))
    status = models.CharField(max_length=10, default="OPEN")
    boosting_type = models.CharField(max_length=10, choices=BOOSTING_TYPE, null=True, default=False)
    time_created = models.DateTimeField(verbose_name="time created", auto_now_add=True)
    booster = models.ForeignKey(Booster, null=True, on_delete=models.SET("deleted"), blank=True)
    order_price = models.IntegerField(default=0, null=False, blank=False)
    account_region = models.CharField(max_length=10, choices=REGIONS, null=False, blank=False)
    discount = models.IntegerField(default=False, null=True)
    is_duo = models.BooleanField(default=False)
    is_flex = models.BooleanField(default=False)
    is_high_priority = models.BooleanField(default=False)
    is_role_champion = models.BooleanField(default=False)
    is_stream = models.BooleanField(default=False)
    promo_code = models.CharField(max_length=10, null=True, default="", blank=True)
    wins_to_play = models.IntegerField(null=True, default=False, blank=True)
    division_from = models.CharField(null=True, max_length=10, choices=DIV, blank=True)
    division_to = models.CharField(null=True, max_length=10, choices=DIV, blank=True)
    league_from = models.CharField(null=True, choices=RANKS, max_length=10, blank=True)
    league_to = models.CharField(null=True, choices=RANKS, max_length=10, blank=True)
    lp_from = models.CharField(null=True, max_length=10, blank=True)
    lp_gain = models.CharField(null=True, max_length=5, blank=True)
    note = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(null=True, default=0)
    booster_gain = models.IntegerField(null=True, default=0)

