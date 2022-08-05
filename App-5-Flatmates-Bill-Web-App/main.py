from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFromPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data

        name1 = bill_form.name1.data
        days_in_house1 = float(bill_form.days_in_house1.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))
        return render_template('bill_form_page.html',billform=bill_form,result = True, name1=flatmate1.name, amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))




class BillForm(Form):
    amount = StringField('Bill Amount: ')
    period = StringField('Bill Period: ')

    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in the house: ')

    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in the house: ')

    button = SubmitField('Calculate')

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.add_url_rule('/bill', view_func=BillFromPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results'))

app.run(debug=True)
