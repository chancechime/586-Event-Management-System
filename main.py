from quick_imports import *
#from ticketsystem.ticketgeneration import ticketgeneration
from ticketsystem.ticket_generation import TicketGenerator
from useraccount.OO_login import login
from useraccount.register import register

#Database = AWS()
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# HOME PAGE
@app.route('/')
def index():
    print("Showing the home page")
    return render_template('index.html')

# EVENTS

## This is the page where the user can see the list of events
@app.route('/events')
def eventsdashboard():
    print("Showing the events page")
    return render_template('events.html')

## This is the page where the user can see the details of the event
@app.route('/events/<event>')
def eventdetails(event):
    print("Showing the event details page for " + event)
    return render_template('eventdetails.html')

## This is the page where the user can select their seatings
@app.route('/events/<event>/reservation')
def eventreservation(event):
    print("Showing the event reservation page for " + event)
    return render_template('eventreservation.html')

## This is the event confirmation page
@app.route('/events/<event>/reservation/confirmation')
def eventconfirmation(event):
    print("Showing the event confirmation page for " + event)
    return render_template('eventconfirmation.html')

# TICKETS

## This is the page where the user can see the list of tickets
### TODO: Redo the tickets page to be come a dashboard for tickets, and for the user to purchase tickets via the EVENTS page.
@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    # Delete/Clear the existing QR code image
    if os.path.exists('static/images/ticketqrcode.png'):
        os.remove('static/images/ticketqrcode.png')
        print("\nDeleted existing QR code image\n")
    if request.method == 'POST':
        ticket_generator = TicketGenerator()
        return ticket_generator.generate_ticket()
    print("Showing the tickets page")
    return render_template('tickets.html')

## This is the page where the user can see the details of the ticket
###! Only accessible if the user is logged in and the ticket belongs to the user
@app.route('/tickets/<ticket>')
def ticketdetails(ticket):
    print("Showing the ticket details page for " + ticket)
    return render_template('ticketdetails.html')

## This redirects the user to a page is shows a printable version of the ticket
@app.route('/tickets/<ticket>/printable')
def ticketprint(ticket):
    print("Showing the printable ticket page for " + ticket)
    return render_template('ticketprint.html')


# USER ACCOUNT/LOGIN/REGISTER

## This is the page where the user can see their account details
@app.route('/account')
def account():
    print("Showing the account page")
    return render_template('account.html')

## This is how the user can logout
@app.route('/logout')
def logout():
    # TODO: Clear the session
    session.pop('username', None)
    print("Logged out")
    return redirect(url_for('index'))

## This is the page where the user can login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect("/")
    print("Showing the login page")
    return render_template('login.html')

## This is the page where the user can register
@app.route('/register')
def register():
    print("Showing the register page")
    return render_template('register.html')

# SUPPORT/LEGAL PAGES

@app.route('/contact')
def contact():
    print("Showing the contact page")
    return render_template('contact.html')

@app.route('/frequently-asked-questions')
def faq():
    print("Showing the FAQ page")
    return render_template('faq.html')

@app.route('/terms-and-conditions')
def terms():
    print("Showing the terms and conditions page")
    return render_template('terms.html')

if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:8080')
    app.run(debug=True, host="localhost", port=8080)