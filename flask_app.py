from flask import Flask, render_template, request, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import data_required, length

app = Flask("_name__")
app.config['SECRET_KEY'] = 'thisismysecretkey'
formData = {}


class EnterName(FlaskForm):
    username = StringField('First Name', validators=[data_required(), length(min=2)])
    password = PasswordField('Password', validators=[data_required(),length(min=3, message="Min 3 Char")])
    submit = SubmitField('Submit')


@app.route("/", methods=['GET', 'POST'])
def home():
    form = EnterName()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        return render_template('output.html', uname=username, password=password)
    else:
        return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
