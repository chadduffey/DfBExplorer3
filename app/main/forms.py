from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class AddUserForm(Form):
    member_email= StringField('Email', validators=[Required(), Email()])
    member_given_name = StringField('Given Name', validators=[Required()])
    member_surname = StringField('Surname', validators=[Required()])
    member_external_id = StringField('(Optional) External Id', validators=[Required()])
    submit = SubmitField('Add Team Member')