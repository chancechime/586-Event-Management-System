from quick_imports import *
from ticketsystem.ticket_generation import TicketGenerator
from useraccount.OO_login import UserAuthentication
from useraccount.register import register
from ticketsystem.event import *
from flask import Flask, render_template, request, redirect, url_for, session, flash
from ticketsystem.event import EventDetails
import json

class BaseHandler:
    """
    Base class for handling Flask routes.
    """
    def __init__(self, app):
        self.app = app

    def register_routes(self):
        """
        Register all routes associated with this handler.
        Override this in subclasses to define specific routes.
        """
        raise NotImplementedError("Subclasses must implement this method")


class HomeHandler(BaseHandler):
    """
    Handles home page and static pages.
    """
    def register_routes(self):
        @self.app.route('/')
        def index():
            print("Showing the home page")
            return render_template('index.html')

        @self.app.route('/contact')
        def contact():
            print("Showing the contact page")
            return render_template('contact.html')

        @self.app.route('/frequently-asked-questions')
        def faq():
            print("Showing the FAQ page")
            return render_template('faq.html')

        @self.app.route('/terms-and-conditions')
        def terms():
            print("Showing the terms and conditions page")
            return render_template('terms.html')


class EventHandler(BaseHandler):
    """
    Handles event-related pages.
    """
    def register_routes(self):
        @self.app.route('/events')
        def events_dashboard():
            print("Showing the events page")
            return render_template('events.html')

        @self.app.route('/events/<int:event_id>')
        def event_details(event_id):
            print(f"Showing the event details page for event #{event_id}")
            event_details = EventDetails(event_id=event_id)
            
            try:
                with open('data/events.json') as file:
                    data = json.load(file)
                
                event_data = next((event for event in data['events'] if event['id'] == event_id), None)
                
                if event_data is None:
                    flash("Event not found", "error")
                    return redirect(url_for('events_dashboard'))
                
                event_details.populate_event(event_data)
                
            except FileNotFoundError:
                flash("Error loading event details", "error")
                return redirect(url_for('events_dashboard'))
            except Exception as e:
                flash(f"Error loading event details: {e}", "error")
                return redirect(url_for('events_dashboard'))
            
            return render_template('eventdetails.html', event_details=event_details)
            
            
        @self.app.route('/events/<event>/reservation')
        def event_reservation(event):
            print(f"Showing the event reservation page for {event}")
            return render_template('eventreservation.html')

        @self.app.route('/events/<event>/reservation/confirmation')
        def event_confirmation(event):
            print(f"Showing the event confirmation page for {event}")
            return render_template('eventconfirmation.html')


class TicketHandler(BaseHandler):
    """
    Handles ticket-related pages.
    """
    def register_routes(self):
        @self.app.route('/tickets', methods=['GET', 'POST'])
        def tickets():
            ticket_generator = TicketGenerator()

            if os.path.exists('static/images/ticketqrcode.png'):
                os.remove('static/images/ticketqrcode.png')
                print("\nDeleted existing QR code image\n")

            if request.method == 'POST':
                return ticket_generator.generate_ticket()

            print("Showing the tickets page")
            return render_template('tickets.html')

        @self.app.route('/tickets/<ticket>')
        def ticket_details(ticket):
            print(f"Showing the ticket details page for {ticket}")
            return render_template('ticketdetails.html')

        @self.app.route('/tickets/<ticket>/printable')
        def ticket_print(ticket):
            print(f"Showing the printable ticket page for {ticket}")
            return render_template('ticketprint.html')


class UserHandler(BaseHandler):
    """
    Handles user account pages and login/logout functionality.
    """
    def __init__(self, app):
        super().__init__(app)
        self.auth = UserAuthentication()

    def register_routes(self):
        @self.app.route('/account')
        def account():
            if 'username' not in session:
                flash("You need to be logged in to view this page", "error")
                return redirect(url_for('login'))
            print("Showing the account page")
            return render_template('account.html')

        @self.app.route('/logout')
        def logout():
            session.pop('username', None)
            print("Logged out")
            return redirect(url_for('index'))

        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                print("Logging in")
                session['username'] = request.form.get('username')
                return self.auth.login()
            return render_template('login.html')

        @self.app.route('/register')
        def register_page():
            print("Showing the register page")
            return render_template('register.html')
        
        @self.app.route('/register_user', methods=['POST'])
        def register_user():
            register()
            return redirect(url_for('login'))

class Application:
    """
    Main application class to configure and start the Flask app.
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = os.urandom(24)
        self.configure_app()

    def configure_app(self):
        self.app.config["SESSION_PERMANENT"] = False
        self.app.config["SESSION_TYPE"] = "filesystem"
        Session(self.app)

    def register_routes(self):
        HomeHandler(self.app).register_routes()
        EventHandler(self.app).register_routes()
        TicketHandler(self.app).register_routes()
        UserHandler(self.app).register_routes()

    def run(self):
        webbrowser.open_new_tab('http://localhost:8080')
        self.app.run(debug=True, host="localhost", port=8080)


if __name__ == '__main__':
    app = Application()
    app.register_routes()
    app.run()