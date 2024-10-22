from flask import Flask, render_template, request
import bcrypt
import re
from AWS import AWS

app = Flask(__name__)

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    checkpw(username, password)
    
    # Checks if user is in the database
    return render_template('login.html')
    connection = "Login Successful" if username in AWS().get_users else "Login Failed. Please try again."
    print(connection) # Output: Login Successful if user is in the database, else Login Failed. Please try again.

def checkpw(username, password):
    # Password -> Hashed Password -> Compares with DB Hashed Password -> Returns True if match, else False
    hashedpw = AWS().get_users(username).hashedpassword
    return True if bcrypt.checkpw(password.encode('utf-8'), hashedpw.encode('utf-8')) else print("Invalid Password")

def register():
    return render_template('register.html')

@app.route('/keyPressEvent', methods=['POST'])
def key_press_event():
    if request.method == 'POST':
        key = request.form.get('key')
        if key == 'Enter':
            login()
            return "Key Press Event Handled"
    print("Invalid Key Press") # Debugging, remove later
    
# Run The App
if __name__ == '__main__':
    app.run(debug=True)