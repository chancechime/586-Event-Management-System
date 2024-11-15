from quick_imports import *
import bcrypt
from flask import request, flash, render_template

class UserAuthentication:
    """
    Handles user authentication logic, including login, password validation, and key press events.
    """
    def __init__(self):
       # self.database = database
        pass

    def login(self):
        """
        Handles user login by validating credentials.
        """
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Username and password are required.", 'warning')
            return "Missing credentials", 400

        if self.check_password(username, password):
            connection = "Login Successful"
        else:
            connection = "Login Failed. Please try again."

        print(connection)  # Debugging output
        flash(connection, 'info')
        return render_template('login.html')

    # def check_password(self, username, password):
    #     """
    #     Validates the user's password by comparing it to the stored hashed password.
    #     """
    #     try:
    #         user_data = self.database.get_users(username)
    #         if user_data and 'hashedpassword' in user_data:
    #             hashed_pw = user_data['hashedpassword']
    #             if bcrypt.checkpw(password.encode('utf-8'), hashed_pw.encode('utf-8')):
    #                 return True
    #             else:
    #                 print("Invalid Password")
    #         else:
    #             print("User not found")
    #     except Exception as e:
    #         print(f"Error in check_password: {e}")
    #     return False

    def register(self):
        """
        Displays the registration page.
        """
        return render_template('register.html')

    def handle_key_press_event(self):
        """
        Handles specific key press events, such as triggering login on 'Enter' key press.
        """
        if request.method == 'POST':
            key = request.form.get('key')
            if key == 'Enter':
                return self.login()
            else:
                print("Invalid Key Press")  # Debugging output
                return "Invalid Key Press", 400
