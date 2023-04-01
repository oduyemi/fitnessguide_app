from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, length, Regexp, Email, EqualTo, ValidationError
from fitnessguide.models import Users


class SignUpForm(FlaskForm):
    fname = StringField("fname",
        validators=[
            DataRequired(),
            length(min=1, max=20, message = "Please provide a valid name"),
            Regexp(
                "^[A-Za-z]x*", 0, "Your First name must contain only letters"
                ),
            ],
        render_kw={"placeholder": "Enter your first name here"})

    lname = StringField("lname",
        validators=[
            DataRequired(),
            length(min=1, max=20, message = "Please provide a valid name"),
            Regexp(
                "^[A-Za-z] [A-Za-a0-9.]*", 0, "Your Last name must contain only letters")],
        render_kw={"placeholder": "Enter your last name here"})

    email = StringField("email",
        validators=
            [DataRequired(),
            length(min=6, max=30),
            Email()],
            render_kw={"placeholder": "Enter your email address"})
    
    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=6, max=20)],
            render_kw={"placeholder": "Enter your password"})
    
    confirm_password = PasswordField("confirm_password",
        validators=
            [DataRequired(),
            length(min=6, max=20)],
            render_kw={"placeholder": "Confirm your password"})
    EqualTo("password", message = "The passwords must match! ")
    submit = SubmitField("Sign Up")
    
    def validate_email(self, email):
        user = Users.query.filter_by(user_email = email.data).first()
        if user:
            raise ValidationError("That email already has an account. Please choose a different one.")


class LoginForm(FlaskForm):
    email = StringField("email",
        validators=
            [DataRequired(),
            length(min=6, max=30),
            Email(),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Enter your email address"})
    
    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=6, max=20)],
            render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class ContactForm(FlaskForm):
    username = StringField("username",
        validators=[
            DataRequired(),
            length(min=2, max=30, message = "Please provide a valid name"),
            Regexp(
                "^[A-Za-z]  [A-Za-z.]*", 0, "Your Last name must contain only letters")],
        render_kw={"placeholder": "Your name"})

    email = StringField("email",
        validators=
            [DataRequired(),
            Email(),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Your email"})

    subject = StringField("subject",
        validators=[
            DataRequired(),
            length(min=2, max=50, message = "Please provide a valid name")],
        render_kw={"placeholder": "Subject"})

    msg = TextAreaField("msg",
        validators=[
            DataRequired(),
            length(min=2, max=1000, message = "Please provide a valid name")],
        render_kw={"placeholder": "Message"})
    
    submit = SubmitField("Send Message")