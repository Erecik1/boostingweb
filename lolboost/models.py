from accounts.models import Account, Booster
from django.db import models

RANKS = (
    ("I", "Iron"),
    ("B", "Bronze"),
    ("S", "Silver"),
    ("G", "Gold"),
    ("P", "Platiuim"),
    ("D", "Diamond"),
    ("M", "Master"),
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
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)
REGIONS = (
    ("1", "EUNE"),
    ("2", "EUW"),
    ("3", "NA"),
    ("4", "RU"),
    ("5", "TR"),
)
QUEUE = (
    ("1", "SOLOQ"),
    ("2", "FLEXQ"),
)

STARTING_LP = (
    ("1","0-20"),
    ("2","21-40"),
    ("3","41-60"),
    ("4","61-80"),
    ("5", "81-100"),

)
FLASH_KEY = (
    ("1", "D"),
    ("2", "F"),
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
    booster = models.ForeignKey(Booster, null=True, on_delete=models.SET("deleted"))
    order_price = models.IntegerField(default=0, null=False)
    account_region = models.CharField(max_length=10, choices=REGIONS, null=False)
    discount = models.IntegerField(default=False, null=True)
    is_duo = models.BooleanField(default=False)
    is_flex = models.BooleanField(default=False)
    is_high_priority = models.BooleanField(default=False)
    is_role_champion = models.BooleanField(default=False)
    is_stream = models.BooleanField(default=False)
    promo_code = models.CharField(max_length=10, null=True, default="")
    wins_to_play = models.IntegerField(null=True, default=False)
    division_from = models.CharField(null=True, max_length=10, choices=DIV)
    division_to = models.CharField(null=True, max_length=10, choices=DIV,)
    league_from = models.CharField(null=True, choices=RANKS, max_length=10)
    league_to = models.CharField(null=True, choices=RANKS, max_length=10)
    lp_from = models.CharField(null=True, choices=STARTING_LP, max_length=10)
    lp_gain = models.CharField(null=True, max_length=10)
