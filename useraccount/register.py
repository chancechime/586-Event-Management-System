from quick_imports import *
import bcrypt
import re
from flask import Flask, request, flash, render_template

class UserRegistration:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/register', methods=['GET', 'POST'])
        def register():
            if request.method == 'POST':
                return self.handle_registration()
            return render_template('register.html')

        @self.app.route('/keyPressEvent', methods=['POST'])
        def key_press_event():
            key = request.form.get('key')
            if key == 'Enter':
                return self.handle_registration()
            print("Invalid Key Press")
            return "Invalid Key Press", 400

    def handle_registration(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not first_name or not last_name or not email or not password or not confirm_password:
            flash("Please fill out all fields.")
        elif not self.check_matching_password(password, confirm_password):
            flash("Passwords do not match.")
        elif not self.is_valid_email(email):
            flash("Invalid email.")
        else:
            hashed_password = self.hash_password(password)
            self.register_user(username, hashed_password, first_name, last_name, email)
            return render_template('login.html')

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, username, hashed_password, first_name, last_name, email):
        if not AWS:
            flash("Database not found.")
            return

        try:
            response = AWS().register_user(username, hashed_password, first_name, last_name, email)
            if response:
                flash("User registered successfully.")
            else:
                flash("Failed to register user.")
        except Exception as e:
            flash("Failed to register user.")
            print(e)

    def is_valid_email(self, email):
        pat = re.compile(r'[\w.-]+@[\w.-]+.\w+')
        return re.match(pat, email) is not None

    def check_matching_password(self, password, confirm_password):
        return password == confirm_password

# Initialize Flask app
app = Flask(__name__)
UserRegistration(app)

if __name__ == '__main__':
    app.run(debug=True)