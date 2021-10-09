from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

# Create your models here.
class UserManager(BaseUserManager):
  
    def create_user(self, name, email, location, phone_number, password=None):

        if name is None:
            raise TypeError('Users should have a name.')
        if email is None:
            raise TypeError('Users should have an email.')
        if location is None:
            raise TypeError('Users should have a location.')
        if phone_number is None:
            raise TypeError('Users should have phone_number.')

        user=self.model(name=name, email=self.normalize_email(email), phone_number=phone_number, location=location)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name,email,phone_number, location, password=None):

        if password is None:
            raise TypeError('This field should not be none.')
        if email is None:
            raise TypeError('Users should have an email.')
        if location is None:
            raise TypeError('Users should have a location.')
        if phone_number is None:
            raise TypeError('Users should have phone_number.')
        
        user=self.create_user(name,phone_number, location, email, )
        user.is_superuser=True
        user.is_staff=True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=30, unique=True, db_index=True)
    email=models.EmailField(max_length=60, unique=True, db_index=True)
    phone_number=models.IntegerField(default=0)
    location=models.CharField(max_length=60, default='no location')
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects=UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''