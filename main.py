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
    return render_template('tickets.html')

if __name__ == '__main__':
    app.run(debug=True)