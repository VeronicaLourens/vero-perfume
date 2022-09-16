from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactUsForm


def contact(request):
    """
    To render and handle the contact form.
    """
    contact_form = ContactUsForm(data=request.POST)
    if request.method == 'POST':
        contact_form = ContactUsForm(data=request.POST)

        if contact_form.is_valid():

            full_name = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            contact = contact_form.save(commit=False)
            contact.save()

            send_mail(
                'Contact us',
                'Thank you for contacting us!',
                'info@veroperfume.com',
                ['info@gmail.com']
            )
            messages.success(request, 'Successfully sent the message!')
            return redirect('home')
    else:
        contact_form = ContactUsForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
