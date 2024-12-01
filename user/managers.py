from django.contrib.auth.models import BaseUserManager


class AdminManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.ADMIN)

class DirectorManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.DIRECTOR)

class DoctorManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.DOCTOR)

class FrontdeskManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.FRONTDESK)

class CashierManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.CASHIER)

class AccauntantManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.ACCAUNTANT)

class PatientManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=self.model.UserType.PATIENT)

