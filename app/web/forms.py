from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class ActivitiesForm(FlaskForm):
    game = SelectField('game', validators=[DataRequired(), Length(1, 10)])
    country = StringField('country', validators=[DataRequired(), Length(1, 2)])
    version = StringField('version', validators=[DataRequired(), Length(1, 5)])
    activity_id = StringField('activity_id', validators=[DataRequired(), Length(1, 8)])
    parameter = StringField('parameter', validators=[DataRequired(), Length(1, 500)])
    period = StringField('period', validators=[DataRequired(), Length(1, 3)])
    submit = SubmitField('Submit')


class PropertiesTranslateForm(FlaskForm):
    properties = FileField('properties', validators=[DataRequired()])
    excel = FileField('excel', validators=[DataRequired()])
    submit= SubmitField('Submit')


class SdataTranslateForm(FlaskForm):
    sdata = StringField('sdata', validators=[DataRequired()])
    excel = StringField('excel', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ExecuteSQLForm(FlaskForm):
    host = StringField('host', validators=[DataRequired()])
    port = StringField('port', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    database = StringField('database', validators=[DataRequired()])
    sql = StringField('sql', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ExecuteBashForm(FlaskForm):
    host = StringField('host', validators=[DataRequired()])
    port = StringField('port', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    bash = StringField('bash', validators=[DataRequired()])
    submit = SubmitField('Submit')
