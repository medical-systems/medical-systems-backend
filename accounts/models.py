from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserRole(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name


class UserInsurance(models.Model):
    insurance_name = models.CharField(max_length=255)

    def __str__(self):
        return self.insurance_name


class UserGender(models.Model):
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.gender


class CustomUserManager(BaseUserManager):
    def doctors(self):
        return self.filter(role__role_name='Doctor')

    def patients(self):
        return self.filter(role__role_name='Patient')

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_num = models.CharField(max_length=255, default="unknown")
    date_of_birth = models.DateField(null=True)
    gender = models.ForeignKey(UserGender, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True)
    insurance = models.ForeignKey(UserInsurance, on_delete=models.SET_NULL, null=True, blank=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username




