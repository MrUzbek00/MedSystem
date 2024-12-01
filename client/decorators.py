from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def is_registered(function):
    def wrapper(request, *args, **kwargs):
        if request.user.gender and request.user.birth_date:
            return(function(request,*args,**kwargs))
        else:
            messages.add_message(request,level=messages.WARNING,message = "Your profile is't complate")
            return redirect(reverse('cl:client_details'))
    return wrapper

