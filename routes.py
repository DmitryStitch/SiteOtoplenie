from flask import render_template, request, flash, redirect, url_for
from app import app, mail
from flask_mail import Message
from forms import ContactForm, QuoteForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()
    quote_form = QuoteForm()
    
    if form.validate_on_submit():
        msg = Message('New Contact Form Submission',
                     sender=form.email.data,
                     recipients=['your-email@gmail.com'])
        msg.body = f"""
        From: {form.name.data}
        Email: {form.email.data}
        Phone: {form.phone.data}
        Message: {form.message.data}
        """
        mail.send(msg)
        flash('Thank you for your message. We will contact you soon!', 'success')
        return redirect(url_for('contacts'))
        
    if quote_form.validate_on_submit():
        msg = Message('New Quote Request',
                     sender=quote_form.email.data,
                     recipients=['your-email@gmail.com'])
        msg.body = f"""
        Quote Request:
        Name: {quote_form.name.data}
        Email: {quote_form.email.data}
        Phone: {quote_form.phone.data}
        Service: {quote_form.service_type.data}
        Details: {quote_form.details.data}
        """
        mail.send(msg)
        flash('Thank you for your quote request. We will contact you shortly!', 'success')
        return redirect(url_for('contacts'))
        
    return render_template('contacts.html', form=form, quote_form=quote_form)
