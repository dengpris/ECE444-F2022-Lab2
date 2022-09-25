from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError

from datetime import datetime

app = Flask( __name__ )
app.config['SECRET_KEY'] = 'wowza!'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):

    def validate_uoft_email(form, field):
        if 'utoronto' not in field.data:
            raise ValidationError('Please enter a utoronto email')

    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT email?', validators=[DataRequired(), Email(), validate_uoft_email])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name, email = None, None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        email = form.email.data
        form.email.data = ''
    return render_template('index.html', form=form, name=name, email=email)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)