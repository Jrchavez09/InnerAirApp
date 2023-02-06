from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError

from inner_air.models import User


class RegisterForm(FlaskForm):
    # validate email
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email exists in db')

    firstname = StringField(label='First Name', validators=[InputRequired(), Length(min=3, max=30)],
                            render_kw={"placeholder": "First Name"})
    email = StringField(label='Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField(label='Password', validators=[InputRequired(), Length(min=8)],
                             render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(label='Confirm Password', validators=[InputRequired(), EqualTo('password')],
                                     render_kw={'placeholder': 'Confirm Password'})
    submit = SubmitField("Sign up")


# Add a class for LoginForm
class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=8)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Sign in")
