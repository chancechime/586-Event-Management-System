# Note: Import send_file, qrcode
from flask_qrcode import QRcode as qr
from flask import Flask, render_template, request
import os
from AWS import AWS

#Database = AWS()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        event = request.form['event']
        quantity = request.form['quantity']
        
        # Generate the QR code with event details
        qr_code_data = f"Event: {event}, Quantity: {quantity}"
        qr.make(qr_code_data).save(os.path.join('static/images', 'ticket.png'))  # Save the QR code

        return render_template('tickets.html')  # Render the tickets page after form submission

    #return render_template('tickets.html')  # Render for GET request

if __name__ == '__main__':
    app.run(debug=True)