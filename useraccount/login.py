from quick_imports import *
import bcrypt
import re

def login():
    username = request.form.get('username')  # Use .get() to avoid KeyError
    password = request.form.get('password')

    if not username or not password:
        flash("Username and password are required.", "danger")
        return redirect(url_for('login'))  # Redirect back to login page

    if checkpw(username, password):
        session['username'] = username
        flash("Login successful!", "success")
        return redirect(url_for('index'))  # Redirect to home page on success
    else:
        flash("Invalid credentials. Please try again.", "danger")
        return redirect(url_for('login'))

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