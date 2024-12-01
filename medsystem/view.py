from django.shortcuts import redirect
from django.urls import reverse

def redirect_view(request):
    if request.user.is_authenticated:
        if request.user.user_type in ['admin','frontdesk']:
            return redirect(reverse('fr:dashboard'))
        if request.user.user_type == 'patient':
            return redirect(reverse('cl:dashboard'))
        if request.user.user_type == 'accauntant':
            return redirect(reverse('ac:dashboard'))
        if request.user.user_type == 'director':
            return redirect(reverse('dr:dashboard'))
        if request.user.user_type == 'cashier':
            return redirect(reverse('ca:dashboard'))
        if request.user.user_type == 'doctor':
            return redirect(reverse('doc:dashboard'))
    else:
        return redirect(reverse('user:login'))