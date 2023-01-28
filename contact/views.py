from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            email = EmailMessage('DjangoShop Message',
            f'Message from {email}\nName: {name}\nContent: {content}','',["mi_email@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?invalid')

    return render(request, 'contact/contact.html', {'contact_form':contact_form})