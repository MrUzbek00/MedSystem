from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

class Service(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    cost = models.FloatField(blank=True,null=True)

class Department(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    head = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='department')
    doctors = models.ManyToManyField('user.CustomUser',blank=True,related_name='department_doctors')

class Ward(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    room_number = models.IntegerField(default=0)
    number_patients = models.IntegerField(default=1)
    number_booked = models.IntegerField(default=0,blank=True)

    @property
    def book_ward(self):
        self.number_booked += 1
        self.save()
    
    @property
    def unregister(self):
        self.number_booked -= 1
        self.save()

    def __str__(self):
        return f"{self.room_number} - {self.department.name}"

class Appointment(models.Model):

    class Type(models.TextChoices):
        OFFLINE = 'ofline'
        ONLINE = 'online'
    
    class Status(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'

    patient = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='appointment_patient')
    doctor = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='appointment_doctor')
    date = models.DateTimeField(blank=True,null=True)
    services = models.ManyToManyField(Service,blank=True)
    status = models.BooleanField(default=False)
    active = models.CharField(max_length=10,choices=Status.choices,default=Status.INACTIVE,blank=True)
    type = models.CharField(max_length=10,choices=Type.choices,default=Type.OFFLINE)


    @property
    def get_invoice(self):
        if self.invoice_set.last():
            return self.invoice_set.last().id
        else:
            return 0

class RegisteredPatients(models.Model):
    ward = models.ForeignKey(Ward,on_delete=models.CASCADE)
    patient = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='registered_patient')
    start_date = models.DateField()
    end_date = models.DateField()

class Notes(models.Model):
    doctor = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='doctor_notes')
    patient = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='patient_notes')
    date = models.DateField(auto_now_add=True)
    note = models.TextField()

class PatientFiles(models.Model):
    file = models.FileField(upload_to = 'patient_files/')
    patient = models.ForeignKey('user.CustomUser',on_delete=models.CASCADE,blank=True,null=True,related_name='patient_files')

    date = models.DateField(auto_now_add=True)

class Invoice(models.Model):

    class Status(models.TextChoices):
        PAID = 'paid'
        UNPAID = 'unpaid'

    class Type(models.TextChoices):
        CARD = 'card'
        CASH = 'cash'

    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=6,blank=True,null=True,choices=Status.choices)
    payment_type = models.CharField(max_length=10,choices=Type.choices,blank=True,null=Type)

