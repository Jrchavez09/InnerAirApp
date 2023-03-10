from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    firstname = StringField(label='First Name', validators=[DataRequired(), Length(min=3, max=20)],
                            render_kw={"placeholder": "First Name"})
    email = StringField(label='Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)],
                             render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={'placeholder': 'Confirm Password'})
    submit = SubmitField("Sign up")


# Add a class for LoginForm
class LoginForm(FlaskForm):
    pass
