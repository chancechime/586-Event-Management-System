from flask import Flask, render_template, request
import qrcode
from AWS import AWS

def ticketgeneration():
    try:
        qr_data = None  # Default QR code data for GET requests
        if request.method == 'POST':
            event = request.form.get('event')
            try:
                quantity = int(request.form.get('quantity'))
            except (ValueError, TypeError):
                quantity = None
            # Check if form data is valid
            if event and quantity:
                # Generate a QR code with event and quantity information
                qr_data = f"Event: {event}, Quantity: {quantity}"
            else:
                qr_data = None
                print("Invalid form data")
        else:
            # Default QR code data for GET requests
            qr_data = None
            print("QR data not found")

        if qr_data is None:
            return "Invalid form data", 400
        else:
            qr_data = "csun.edu"
            img = qrcode.make(qr_data)
            img.save('static/images/ticketqrcode.png')
        
        print(f"\n\tQR code generated with data: {qr_data}\n")
        # Ensure render_template is always reached
        return render_template('tickets.html', qr_data="static/images/ticketqrcode.png")
    except Exception as e:
        # Log the exception and return an error page or message if needed
        print(f"Error in tickets route: {e}")
        return "An error occurred", 500