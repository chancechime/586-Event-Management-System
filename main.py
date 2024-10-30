from quick_imports import *
from ticketsystem.ticketgeneration import ticketgeneration
from useraccount.login import login
from useraccount.register import register

#Database = AWS()
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/logout')
def logout():
    
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect("/")
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    # Delete/Clear the existing QR code image
    if os.path.exists('static/images/ticketqrcode.png'):
        os.remove('static/images/ticketqrcode.png')
        print("\nDeleted existing QR code image\n")
    if request.method == 'POST':
        return ticketgeneration()
    return render_template('tickets.html')

if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:8080')
    app.run(debug=True, host="localhost", port=8080)