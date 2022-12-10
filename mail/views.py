from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from mail.forms import ContactForm

# Create your mail/views here.


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data['message']
            email_subject = f'New contact {email}: {subject}'
            email_message = message
            try:
                send_mail(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, 'mail/success.html')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'mail/contact.html', context=context)
