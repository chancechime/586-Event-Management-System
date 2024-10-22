# Note: Import send_file, qrcode

from flask import Flask 
from AWS import AWS
# app = create_app()

Database = AWS()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)