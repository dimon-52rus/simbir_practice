# -*- coding: utf-8 -*-

#from wtforms import Form, StringField, validators
from wtforms import Form
from wtforms import (StringField)
from wtforms.validators import InputRequired, Length

class LoginForm(Form):
#    username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
#    password = StringField('Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
#    email = StringField('Email:', validators=[validators.optional(), validators.Length(min=0, max=50)])
    username = StringField('Username:', validators=[InputRequired(), Length(min=5, max=30)])
    password = StringField('Password:', validators=[InputRequired(), Length(min=5, max=30)])
    email = StringField('Email:', validators=[Length(min=0, max=30)])
