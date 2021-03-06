from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Hospital

STATE_ABBREV = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD', 
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class EditUserProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contact = StringField('Phone Number')

    submit = SubmitField('Save')

class VerifyForm(FlaskForm):
    submit = SubmitField('Verify')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    hospital_name = SelectField('Hospital', coerce=int)
    contact = StringField('Phone Number', validators=[DataRequired()])
    street = StringField('Street Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[(state, state) for state in STATE_ABBREV], default="WA")
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Register')
class EditHospitalProfileForm(FlaskForm):
    street = StringField('Street Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[(state, state) for state in STATE_ABBREV], default="WA")
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Save')


class ResetPassword(FlaskForm):
    email = StringField("Enter your user account's verified email address and we will send you a password reset link.", validators=[DataRequired(), Email()])
    submit = SubmitField('Send password reset email')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No user exists with that email')

class HospitalInformation(FlaskForm):
    hospitalID = StringField("Enter Hospital ID", validators=[DataRequired()])
    submit = SubmitField('Search')

    def validate_hospitalID(self, hospitalID):
        HospitalRow = Hospital.query.filter_by(id=hospitalID.data).first()
        if HospitalRow is None:
            raise ValidationError('Invalid ID')


class ChangePassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update Password')
