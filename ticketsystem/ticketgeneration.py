import qrcode as qr
from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    qr.make("123456789").save("../static/images/ticket.png")  # Save in the static directory
    if request.method == 'POST':
        # Handle ticket purchase here if needed
        pass
    return render_template('tickets.html')  # Render the tickets page
    return send_file("../static/images/ticket.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)