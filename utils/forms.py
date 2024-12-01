from .models import Department,Ward,Appointment,RegisteredPatients,Notes,PatientFiles
from django import forms



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = '__all__'


class RegisterPatient(forms.ModelForm):
    class Meta:
        model = RegisteredPatients
        fields = '__all__'


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'

class FileForm(forms.ModelForm):
    class Meta:
        model = PatientFiles
        fields = '__all__'