import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
  'secret_key': 'sk_test_fefrdLARpjWhTCTP8pi5kCal',
  'publishable_key': 'pk_test_gRs324976vkdBuenifKpj6z5'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    amount = int(float(request.form['amount'])*100)#500
    print amount,request.form['amount']
    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='eur',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
  app.run(debug=True)