from quick_imports import *
import bcrypt
from flask import request, flash, render_template

class UserAuthentication:
    def __init__(self):
        pass

    def login(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Username and password are required.", 'warning')
            return "Missing credentials", 400

        if self.check_password(username, password):
            connection = "Login Successful"
        else:
            connection = "Login Failed. Please try again."

        print(connection)
        flash(connection, 'info')
        return render_template('login.html')

    def check_password(self, username, password):
        try:
            user_data = self.database.get_users(username)
            if user_data and 'hashedpassword' in user_data:
                hashed_pw = user_data['hashedpassword']
                if bcrypt.checkpw(password.encode('utf-8'), hashed_pw.encode('utf-8')):
                    return True
                else:
                    print("Invalid Password")
            else:
                print("User not found")
        except Exception as e:
            print(f"Error in check_password: {e}")
        return False

    def register(self):
        return render_template('register.html')

    def handle_key_press_event(self):
        if request.method == 'POST':
            key = request.form.get('key')
            if key == 'Enter':
                return self.login()
            else:
                print("Invalid Key Press")
                return "Invalid Key Press", 400