from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
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

            html = render_to_string(
                'contact/email.html', {
                    'full_name': full_name,
                    'email': email,
                    'message': message
                }
            )

            contact_form = contact_form.save(commit=False)
            contact_form.save()

            send_mail(
                'Contact us',
                'Thank you for contacting us!',
                'info@veroperfume.com',
                ['user@email.com'],
                html_message=html
            )
            messages.success(request, 'Successfully sent the message!')
            return redirect('home')
    else:
        contact_form = ContactUsForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
