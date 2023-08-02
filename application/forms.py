from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddPokemonForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    ability = StringField("Ability", validators=[DataRequired(), Length(min=2, max=50)])
    type = StringField("Type", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Add Pokemon")
