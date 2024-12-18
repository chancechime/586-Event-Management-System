from quick_imports import *
import bcrypt
from flask import request, flash, render_template
import boto3
from botocore.exceptions import ClientError

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
            session['username'] = username
            connection = "Login Successful"
            return render_template('index.html')
        else:
            connection = "Login Failed. Please try again."
        
        print(connection)  # Debugging output
        flash(connection, 'info')
        return render_template('login.html')
    
    def get_secret(self,username):
        secret_name = username
        region_name = "us-west-1"

    # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e

        secret = get_secret_value_response['SecretString']
    def check_password(self, username, password):
        aws_password = self.get_secret(username)
        if not aws_password:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), aws_password.encode('utf-8'))
  

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