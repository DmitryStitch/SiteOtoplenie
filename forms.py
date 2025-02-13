from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Телефон', validators=[DataRequired()])
    message = TextAreaField('Сообщение', validators=[DataRequired()])

class QuoteForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Телефон', validators=[DataRequired()])
    service_type = SelectField('Тип услуги', choices=[
        ('heating_installation', 'Установка системы отопления'),
        ('maintenance', 'Техническое обслуживание'),
        ('repair', 'Ремонтные работы'),
        ('consultation', 'Консультация')
    ])
    details = TextAreaField('Детали проекта', validators=[DataRequired()])