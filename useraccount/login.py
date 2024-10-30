from quick_imports import *
import bcrypt
import re

def login():
    username = request.form['username']
    password = request.form['password']
    checkpw(username, password)
    
    # Checks if user is in the database
    connection = "Login Successful" if username in AWS().get_users else "Login Failed. Please try again."
    print(connection) # Output: Login Successful if user is in the database, else Login Failed. Please try again.
    flash(connection, 'info')
    #return render_template('login.html')
    

def checkpw(username, password):
    # Password -> Hashed Password -> Compares with DB Hashed Password -> Returns True if match, else False
    try:
        hashedpw = AWS().get_users(username).hashedpassword
        return True if bcrypt.checkpw(password.encode('utf-8'), hashedpw.encode('utf-8')) else print("Invalid Password")
    except Exception as e:
        print(f"Error in checkpw: {e}")
        return False

def register():
    return render_template('register.html')

def key_press_event():
    if request.method == 'POST':
        key = request.form.get('key')
        if key == 'Enter':
            login()
            return "Key Press Event Handled"
    print("Invalid Key Press") # Debugging, remove later
    return "Invalid Key Press", 400