from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])

class QuoteForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    service_type = SelectField('Service Type', choices=[
        ('heating_installation', 'Heating System Installation'),
        ('maintenance', 'System Maintenance'),
        ('repair', 'Repair Services'),
        ('consultation', 'Consultation')
    ])
    details = TextAreaField('Project Details', validators=[DataRequired()])
