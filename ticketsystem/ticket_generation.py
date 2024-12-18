from quick_imports import *

class TicketGenerator:
    def __init__(self, qr_image_path='static/images/ticketqrcode.png'):
        self.qr_image_path = qr_image_path

    def generate_ticket(self):
        """
        Main method to generate a ticket based on request data.
        """
        try:
            if request.method == 'POST':
                event = request.form.get('event')
                quantity = self.get_quantity(request.form.get('quantity'))

                if event and quantity is not None:
                    qr_data = f"Event: {event}, Quantity: {quantity}"
                    self.create_qr_code(qr_data)
                    return render_template(
                        'tickets.html', 
                        qr_data=self.qr_image_path, 
                        event=event, 
                        quantity=quantity
                    )
                else:
                    return "Invalid form data", 400
            else:
                return render_template('tickets.html', qr_data=None)
        except Exception as e:
            print(f"Error in ticket generation: {e}")
            return "An error occurred", 500

    def get_quantity(self, quantity):
        """
        Helper method to validate and convert quantity.
        """
        try:
            return int(quantity)
        except (ValueError, TypeError):
            return None

    def create_qr_code(self, data):
        """
        Generates and saves a QR code image with the specified data.
        """
        img = qrcode.make(data)
        img.save(self.qr_image_path)


ticket_generator = TicketGenerator()