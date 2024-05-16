from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange


class PetForm(FlaskForm):
    """Form to be displayed to user for adding and editing pets."""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo_url = URLField("Image URL", validators=[Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Availability")
