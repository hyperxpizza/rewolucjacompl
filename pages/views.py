from django.shortcuts import render, redirect, HttpResponse
from .models import ArtImage, IndexSliderImage
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def about(request):
    images = IndexSliderImage.objects.order_by('uploaded_at')
    context ={
        'images': images
    }
    return render(request, 'pages/about.html', context)

def art(request):
    images = ArtImage.objects.order_by('uploaded_at')
    context={
        'images':images
    }
    return render(request, 'pages/art.html', context)

def contact_mail(request):
    if request.method =="GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            subject2 = "Kontakt - Studio Rewolucja"
            message2 = "Dziękujemy za wiadomość! Postaramy się odpowiedzieć na twojego maila w jak najkrótszym czasie. TEAM REWOLUCJA."

            try:
                send_mail(subject,message, from_email, ["studio.rewolucja@gmail.com"])
                send_mail(subject2, message2, "studio.rewolucja@gmail.com", [from_email])
            except BadHeaderError:
                return HttpResponse('Invalid header')
            
            return redirect('pages:contact_success')
    
    context = {
        'form': form
    }

    return render(request, 'pages/contact_mail.html', context)    


def contact_success(request):
    context = {}
    return render(request, 'pages/success.html', context)
