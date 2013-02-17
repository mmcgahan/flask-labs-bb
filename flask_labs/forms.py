from wtforms.ext.sqlalchemy.orm import model_form
from flaskext.wtf import (Form, TextField, PasswordField, BooleanField,
    QuerySelectField, SubmitField, HiddenField, validators)
from flask_labs.models import User, Post, Quotation, Registry

UserFormBase = model_form(
    User, Form, only=['first_name', 'last_name', 'active']
)
EditorFormBase = model_form(Post, Form)
QuotationFormBase = model_form(Quotation)
RegistryFormBase = model_form(Registry)


class LoginForm(Form):
    username = TextField('Username')
    raw_password = PasswordField('Password')
    next = HiddenField()
    submit = SubmitField('Log in')


class UserForm(UserFormBase):
    raw_password = PasswordField('Reset password',
        [validators.EqualTo('raw_password2', message='Passwords must match')
    ])
    raw_password2 = PasswordField('Confirm password')
    next = HiddenField()
    submit = SubmitField('Save')


class EditUserForm(UserForm):
    username = TextField('Username', [validators.Required()])
    submit = SubmitField('Save')


class CreateUserForm(EditUserForm):
    raw_password = PasswordField('Set password',
        [validators.EqualTo('raw_password2', message='Passwords must match'),
        validators.Length(min=6),
        validators.Required()
    ])
    submit = SubmitField('Create')


class EditorForm(EditorFormBase, QuotationFormBase):
    author = QuerySelectField(query_factory=User.query.all, get_label='username')
    submit = SubmitField('Update')


class RegistryForm(RegistryFormBase):
    book_title = TextField('Title')
    book_author = TextField('Author')
    is_special = BooleanField('Special?')
    submit = SubmitField('Add')
