from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterUserForm,RegistrationForm
from django.contrib.auth import login,authenticate,logout

def register_user(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST,request.FILES)
        # nevergiveup3
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'User added')
        else:
            messages.add_message(request,messages.ERROR,form.errors)
    return redirect(url)

def _login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            if user.user_type in ['admin','frontdesk']:
                return redirect(reverse('fr:dashboard'))
            if user.user_type == 'patient':
                return redirect(reverse('cl:dashboard'))
            if user.user_type == 'cashier':
                return redirect(reverse('ca:dashboard'))
            if user.user_type == 'doctor':
                return redirect(reverse('doc:dashboard'))
            if user.user_type == 'accauntant':
                return redirect(reverse('ac:dashboard'))
            if user.user_type == 'director':
                return redirect(reverse('dr:dashboard'))
    return render(request,'login.html')

def _logout(request):
    logout(request)
    return redirect(reverse('user:login'))

def register(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'patient'
            user.save()
            login(request,user)
            return redirect(reverse('cl:dashboard'))
        else:
            messages.add_message(request,messages.ERROR,form.errors)
    return redirect(url)
