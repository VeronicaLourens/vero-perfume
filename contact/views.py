from django.shortcuts import render
from .models import ContactUs
from django.http import JsonResponse


def contact_us(request):
    """
    To render and handle the contact form.
    """
    # if request.POST.get('action') == 'post':
    #     email = request.POST.get('email')
    #     content = request.POST.get('content')
    #     ContactUs.objects.create(email=email, content=content)
       
    #     messages.success(request, 'Successfully sent the message!')
        

    return render(request, 'contact/contact_us.html')