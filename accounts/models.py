from typing import ChainMap
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import Choices

class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("user must have an email address.")
        if not username:
            raise ValueError("user must have a username.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password = password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f"profile_images/{self.pk}/profile_image.png"

def get_default_profile_image():
    return "default_image/profile_image.png"



class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_booster = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_default_profile_image, null=True, blank=True, default=get_default_profile_image)


    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Booster(models.Model):
    LANGUAGES = (
        ("EN","English"),
        ("PL","Polish"),
        ("KR","Korean"),
    )
    REGIONS = (
        ("EUNE","EUNE"),
        ("EUW","EUW"),
        ("NA","NA"),
        ("RU","RU"),
        ("TR","TR"),
    )
    account = models.ForeignKey(Account,null=False, on_delete=CASCADE, default="")
    about = models.CharField(max_length=512)
    rank = models.CharField(max_length=30,)
    roles = models.CharField(max_length=30,)
    champions = models.CharField(max_length=30,)
    status = models.BooleanField(default=False)
    reviews = models.IntegerField()
    regions = models.CharField(max_length=30, choices=REGIONS)
    orders_done = models.IntegerField()
    languages = models.CharField(max_length=30,choices=LANGUAGES)

    def __str__(self):
        return self.account
