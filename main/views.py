
from django.shortcuts import render, redirect
from .forms import ContactForm, QuoteForm
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contacts(request):
    contact_form = ContactForm()
    quote_form = QuoteForm()
    
    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                # Обработка формы контакта
                messages.success(request, 'Сообщение успешно отправлено!')
                return redirect('contacts')
        elif 'quote_submit' in request.POST:
            quote_form = QuoteForm(request.POST)
            if quote_form.is_valid():
                # Обработка формы заявки
                messages.success(request, 'Заявка успешно отправлена!')
                return redirect('contacts')
    
    return render(request, 'contacts.html', {
        'contact_form': contact_form,
        'quote_form': quote_form
    })
