from quick_imports import *
import qrcode
from flask import request, render_template

class TicketGenerator:
    def __init__(self, qr_image_path='static/images/ticketqrcode.png'):
        self.qr_image_path = qr_image_path
        self.qr_data = None

    def generate_ticket(self):
        try:
            if request.method == 'POST':
                self.process_post_request()
            else:
                self.qr_data = None
                print("QR data not found for GET request")

            if self.qr_data is None:
                return "Invalid form data", 400
            else:
                self.create_qr_code(self.qr_data)
                print(f"\n\tQR code generated with data: {self.qr_data}\n")
                return render_template('tickets.html', qr_data=self.qr_image_path)
        except Exception as e:
            print(f"Error in ticket generation: {e}")
            return "An error occurred", 500

    def process_post_request(self):
        event = request.form.get('event')
        quantity = self.get_quantity(request.form.get('quantity'))

        if event and quantity is not None:
            self.qr_data = f"Event: {event}, Quantity: {quantity}"
        else:
            self.qr_data = None
            print("Invalid form data in POST request")

    def get_quantity(self, quantity):
        try:
            return int(quantity)
        except (ValueError, TypeError):
            return None

    def create_qr_code(self, data):
        img = qrcode.make(data)
        img.save(self.qr_image_path)