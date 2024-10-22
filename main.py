# Note: Import send_file, qrcode
from flask import Flask, send_file

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)