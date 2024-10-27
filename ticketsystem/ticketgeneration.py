from flask import Flask, render_template, request
from flask_qrcode import QRcode
from AWS import AWS

app = Flask(__name__)
QRcode(app)

@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    try:
        qr_data = "No ticket data available."  # Default QR code data for GET requests

        if request.method == 'POST':
            event = request.form.get('event')
            quantity = request.form.get('quantity')
            
            # Check if form data is valid
            if event and quantity:
                # Generate a QR code with event and quantity information
                qr_data = f"Event: {event}, Quantity: {quantity}"
            else:
                qr_data = "Invalid ticket data."

        # Ensure render_template is always reached
        response = render_template('tickets.html', qr_data=qr_data)
        if response is None:
            raise ValueError("render_template returned None. Check if 'tickets.html' exists and is valid.")
        return response
    
    except Exception as e:
        # Log the exception and return an error page or message if needed
        print(f"Error in tickets route: {e}")
        return "An error occurred", 500

if __name__ == '__main__':
    app.run(debug=True)