from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AdminManager,DoctorManager,DirectorManager,FrontdeskManager,CashierManager,AccauntantManager,PatientManager


class CustomUser(AbstractUser):

    class UserType(models.TextChoices):
        ACCAUNTANT = 'accauntant'
        FRONTDESK = 'frontdesk'
        DIRECTOR = 'director'
        PATIENT = 'patient'
        CASHIER = 'cashier'
        DOCTOR = 'doctor'
        ADMIN = 'admin'
    
    class GenderType(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'
    
    image = models.ImageField(upload_to='UserImages/',blank=True,null=True)
    phone = models.CharField(max_length = 20, blank=True, null=True)
    gender = models.CharField(max_length = 6, choices = GenderType.choices, blank=True,null=True)

    region = models.CharField(max_length = 30, blank=True, null=True)
    city = models.CharField(max_length = 30, blank=True, null=True)
    address = models.CharField(max_length = 100, blank=True, null=True)

    passport_id = models.CharField(max_length=20,blank=True,null=True,unique=True)
    birth_date = models.DateField(blank=True,null=True)
    specialization = models.CharField(max_length=200,blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    service_type = models.ManyToManyField('utils.Service',blank=True)
    registered_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    meeting = models.URLField(blank=True,null=True)
    user_type = models.CharField(max_length = 25, choices = UserType.choices, default= UserType.ADMIN)

    @property
    def is_registered(self):
        return bool(self.phone and self.gender and self.region and self.address and self.first_name and self.last_name)


    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''

    REQUIRED_FIELDS = []

    def save(self,*args,**kwargs):
        if not self.username:
            self.username = self.passport_id
            
        if self.password and not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        return super().save(*args,**kwargs)


class Admin(CustomUser):
    objects = AdminManager()

    class Meta:
        proxy = True

class Director(CustomUser):
    objects = DirectorManager()

    class Meta:
        proxy = True

class Doctor(CustomUser):
    objects = DoctorManager()

    class Meta:
        proxy = True

class Frontdesk(CustomUser):
    objects = FrontdeskManager()
    class Meta:
        proxy = True

class Cashier(CustomUser):
    objects = CashierManager()
    class Meta:
        proxy = True

class Accauntant(CustomUser):
    objects = AccauntantManager()

    class Meta:
        proxy = True

class Patient(CustomUser):
    objects = PatientManager()

    class Meta:
        proxy = True


