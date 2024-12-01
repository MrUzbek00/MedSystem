from django.shortcuts import render,redirect
from django.urls import reverse
from utils.models import Invoice,Department,Appointment
from django.utils import timezone
from django.db.models import Sum
from django.http import HttpResponse
from openpyxl import Workbook


def dashboard(request):
    today = timezone.now()
    invoices = Invoice.objects.filter(created_date__year = today.year, created_date__day = today.day)
    departments = Department.objects.all()

    status,department = request.GET.get('status',None),request.GET.get('department',None)

    if status:
        invoices = invoices.filter(status = status)
    if department:
        selected_department = Department.objects.get(id = department)
        invoices = invoices.filter(
                    appointment__doctor__department=selected_department
                )


    context = {
        'invoices':invoices,
        'departments':departments,
    }

    return render(request,'cashier/cashier.html',context)

def invoice(request,id):

    invoice = Invoice.objects.get(id = id)

    if request.method == 'POST':
        payment_type = request.POST.get('paymet_type')
        invoice.payment_type = payment_type
        invoice.status = 'paid'
        invoice.appointment.active = 'active'
        invoice.appointment.save()
        invoice.save()

        return redirect(reverse('ca:dashboard'))

    context = {
        'invoice':invoice
    }

    return render(request,'cashier/invoice.html',context)

def generate_report(request):
    # Get current date
    current_date = timezone.now()
    
    # Calculate start and end dates for weekly, monthly, and yearly reports
    weekly_start_date = current_date - timezone.timedelta(days=current_date.weekday())
    weekly_end_date = weekly_start_date + timezone.timedelta(days=6)
    monthly_start_date = current_date.replace(day=1)
    monthly_end_date = monthly_start_date.replace(day=timezone.now().month + 1, hour=0, minute=0, second=0)
    yearly_start_date = current_date.replace(month=1, day=1)
    yearly_end_date = current_date.replace(month=12, day=31, hour=23, minute=59, second=59)

    # Query for appointments and invoices for each period
    weekly_appointments = Appointment.objects.filter(date__range=[weekly_start_date, weekly_end_date]).annotate(amount = Sum('services__cost'))
    monthly_appointments = Appointment.objects.filter(date__range=[monthly_start_date, monthly_end_date]).annotate(amount = Sum('services__cost'))
    yearly_appointments = Appointment.objects.filter(date__range=[yearly_start_date, yearly_end_date]).annotate(amount = Sum('services__cost'))

    # Calculate statistics
    weekly_total_appointments = weekly_appointments.count()
    monthly_total_appointments = monthly_appointments.count()
    yearly_total_appointments = yearly_appointments.count()

    weekly_total_paid = weekly_appointments.filter(invoice__status=Invoice.Status.PAID).count()
    monthly_total_paid = monthly_appointments.filter(invoice__status=Invoice.Status.PAID).count()
    yearly_total_paid = yearly_appointments.filter(invoice__status=Invoice.Status.PAID).count()

    weekly_total_unpaid = weekly_total_appointments - weekly_total_paid
    monthly_total_unpaid = monthly_total_appointments - monthly_total_paid
    yearly_total_unpaid = yearly_total_appointments - yearly_total_paid

    weekly_total_amount = weekly_appointments.aggregate(total = Sum('amount'))['total']
    monthly_total_amount = monthly_appointments.aggregate(total = Sum('amount'))['total']
    yearly_total_amount = yearly_appointments.aggregate(total = Sum('amount'))['total']

    # Create Excel workbook
    wb = Workbook()
    ws = wb.active

    # Populate Excel sheet with data
    ws.append(["Period", "Total Appointments", "Total Paid", "Total Unpaid", "Total Amount"])
    ws.append(["Weekly", weekly_total_appointments, weekly_total_paid, weekly_total_unpaid, weekly_total_amount])
    ws.append(["Monthly", monthly_total_appointments, monthly_total_paid, monthly_total_unpaid, monthly_total_amount])
    ws.append(["Yearly", yearly_total_appointments, yearly_total_paid, yearly_total_unpaid, yearly_total_amount])

    # Save workbook to response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=appointment_report.xlsx'
    wb.save(response)
    return response
