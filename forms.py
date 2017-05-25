from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    firstname= StringField("First name", validators=[DataRequired("Please enter your first name.")])
    lastname= StringField("Last name",validators=[DataRequired("Please enter your last name.")])
    email= StringField("Email",validators=[DataRequired("Pleasae enter your email."), Email("Please, enter your email address.")])
    password=PasswordField("Password",validators=[DataRequired("Please enter your password."), Length(min=6, message="Password must be more than 6 characters.")])
    sumbit=SubmitField("Sign Up",validators=[DataRequired()])

class LoginForm(Form):
    email=StringField('Email', validators=[DataRequired("Please enter email address."), Email("Please enter you email.")])
    password=PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit=SubmitField("Sign in")

class AddressForm(Form):
    address=StringField('Address', validators=[DataRequired("Please enter an address")])
    submit=SubmitField("Search")
