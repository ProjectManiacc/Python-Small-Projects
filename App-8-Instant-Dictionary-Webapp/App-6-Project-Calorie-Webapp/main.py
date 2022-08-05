from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(calories_form.country.data, calories_form.city.data).get()
        calorie = Calorie(float(calories_form.weight.data), float(calories_form.height.data),
                          float(calories_form.age.data), temperature)

        calories = calorie.calculate()
        return render_template('calories_form_page.html', caloriesform=calories_form, calories=calories, result=True)


class CaloriesForm(Form):
    weight = StringField('Weight: ')
    height = StringField('height: ')
    age = StringField('Age: ')
    city = StringField('City: ')
    country = StringField('Country: ')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results'))

app.run(debug=True)
