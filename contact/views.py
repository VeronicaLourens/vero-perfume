from django.shortcuts import render
from .models import ContactUs


def contact(request):
    """
    To render and handle the contact form.
    """
    # if request.method == POST:
    #     contact_form = ContactUsForm(data=request.POST)
    #     if contact_form.is_valid():
            
    #         contact = contact_form.save(commit=False)
    #         contact.save()
    #         messages.success(request, 'Successfully sent the message!')
    #         return redirect('home')

    #     else:
    #         contact_form = ContactUsForm()

    # context = {
    #     'contact_form': contact_form,
    # }

    return render(request, 'contact/contact.html')