from accounts.models import Account, Booster
from django.db import models

RANKS = (
    ("I","Iron"),
    ("B","Bronze"),
    ("S","Silver"),
    ("G","Gold"),
    ("P","Platiuim"),
    ("D","Diamond"),
    ("M","Master"),
)

DIV = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
)
REGIONS = (
    ("EUNE","EUNE"),
    ("EUW","EUW"),
    ("NA","NA"),
    ("RU","RU"),
    ("TR","TR"),
)
QUEUE = (
    ("SOLOQ","SOLOQ"),
    ("FLEXQ","FLEXQ"),
)
FLASH_KEY = (
    ("D","D"),
    ("F","F"),
)
STATUS = (
    ("PENDING","PENDING"),
    ("OPEN","OPEN"),
    ("DONE","DONE")
)

class Order(models.Model):
    user = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, default="OPEN")
    time_created = models.DateTimeField(verbose_name="time created", auto_now_add=True)
    booster = models.ForeignKey(Booster,null=True, on_delete=models.SET("deleted"))

class DivisionBoosting(models.Model):
    order_id = models.ForeignKey(Order,null=True, on_delete=models.SET_NULL)
    queue = models.CharField(max_length=10,choices=QUEUE)
    start_rank = models.CharField(max_length=10,choices=RANKS)
    start_div = models.CharField(max_length=10, choices=DIV)
    start_lp = models.IntegerField()
    gain_lp = models.IntegerField()
    end_rank = models.CharField(max_length=10,choices=RANKS)
    end_div = models.CharField(max_length=10, choices=DIV)
    flash_key = models.CharField(max_length=1, choices=FLASH_KEY, default="F")
    server = models.CharField(max_length=10,choices=REGIONS, null=True)

class WinBoosting(models.Model):
    order_id = models.ForeignKey(Order,null=True, on_delete=models.SET_NULL)
    queue = models.CharField(max_length=10,choices=QUEUE)
    start_rank = models.CharField(max_length=10,choices=RANKS)
    start_div = models.CharField(max_length=10, choices=DIV)
    start_lp = models.IntegerField()
    gain_lp = models.IntegerField()
    win_expected = models.IntegerField()
    flash_key = models.CharField(max_length=1, choices=FLASH_KEY, default="F")
    server = models.CharField(max_length=10,choices=REGIONS, null=True)

class PlacementBoosting(models.Model):
    order_id = models.ForeignKey(Order,null=True, on_delete=models.SET_NULL)
    queue = models.CharField(max_length=10,choices=QUEUE)
    previous_rank = models.CharField(max_length=10,choices=RANKS)
    previous_div = models.IntegerField(choices=DIV)
    match_numbers = models.IntegerField()
    flash_key = models.CharField(max_length=1, choices=FLASH_KEY, default="F")
    server = models.CharField(max_length=10,choices=REGIONS, null=True)
