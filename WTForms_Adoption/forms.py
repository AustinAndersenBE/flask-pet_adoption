from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, validators

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', [validators.InputRequired()])
    species = StringField('Species', [
        validators.InputRequired(),
        validators.AnyOf(['cat', 'dog', 'porcupine'], "Species must be either 'cat', 'dog', or 'porcupine'")
        ])
    photo_url = StringField('Photo URL', [
        validators.Optional(),
        validators.URL(message="Must be a valid URL")
    ])
    age = IntegerField('Age', [
        validators.Optional(),
        validators.NumberRange(min=0, max=30, message="Age must be between 0 and 30.")
    ])
    notes = StringField('Notes')
    submit = SubmitField('Add Pet')

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', [
        validators.Optional(),
        validators.URL(message="Must be a valid URL")
    ])
    notes = StringField('Notes')
    available = BooleanField('Available')
    submit = SubmitField('Update Pet')
