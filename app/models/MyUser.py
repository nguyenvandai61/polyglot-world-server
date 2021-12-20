from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from config import POLYGLOT_CLOUDINARY_URL

from .Language import Language
from .LearnProgress import LearnProgress


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )
        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )
        user.username = username
        user.set_password(password)
        email = extra_fields.pop('email', None)
        first_name = extra_fields.pop('first_name', None)
        last_name = extra_fields.pop('last_name', None)
        country = extra_fields.pop('country', None)
        avatar = extra_fields.pop('avatar', None)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.country = country

        default_learn_progress = LearnProgress()
        default_learn_progress.save()
        user.learn_progress = default_learn_progress

        if avatar:
            user.avatar = avatar
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.CharField(
        max_length=200, default=POLYGLOT_CLOUDINARY_URL+"/avatars/default/default-avatar_n5b5k4.png")
    gender = models.BooleanField(default=1)

    country = models.CharField(max_length=30, default='Viet Nam')
    languages = models.ManyToManyField(Language, related_name='languages')

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    learn_progress = models.OneToOneField(
        LearnProgress, on_delete=models.CASCADE, null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

    def get_by_natural_key(self, username):
        return self.get(username=username)

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
