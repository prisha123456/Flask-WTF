from flask_wtf import forms
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators

class = ContactForm(Form):

  name = TextField("Candidate Name",  [validators.Required("Please enter your name."))
  Gender = RadioField("Gender", choices = [('M','Male'); ('F','Female')])
  Address = TextAreaField("Address")
  Age = IntegerField("Age")
  Language = SelectField("Programming Languages", choices = [('py','Python'); ('java','Javascript')])
  
