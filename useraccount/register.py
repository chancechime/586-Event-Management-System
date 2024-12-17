from quick_imports import *
import bcrypt
import re
import pymssql

app = Flask(__name__)
conn = pymssql.connect(server='ems.cp084oyu2d47.us-west-1.rds.amazonaws.com', user='admin', password='L33?Af6K}Pxx9e!s%CabSo_w*|$q', database='ems')
cursor = conn.cursor()
# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        print("password"+request.form['password'])
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if not first_name or not last_name or not email or not password or not confirm_password:
            flash("Please fill out all fields.")
        elif not check_matching_password(password, confirm_password):
            flash("Passwords do not match.")
        elif not is_valid_email(email):
            flash("Invalid email.")
    hashed_password = hash_password(password)
    register_user(username, password, first_name, last_name, email)

@app.route('/keyPressEvent', methods=['POST'])
def key_press_event():
    key = request.form.get('key')
    if key == 'Enter':
        return register()
    print("Invalid Key Press")
    return "Invalid Key Press", 400

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def register_user(username, hashed_password, first_name, last_name, email):
    if not AWS:
        flash("Database not found.")
        return
    
    try:
        cursor2 = Database()

        query= "INSERT INTO user_credentials (username, hashed_password, first_name, last_name, email) VALUES ('"+ username +"','"+ hashed_password +"','"+ first_name +"','"+ last_name + "','"+ email +"')"
        print(query)
        cursor.execute(query)
        conn.commit()
        print("here")
        # flash("User registered successfully.")
        
    except Exception as e:
        flash("Failed to register user.")
        print(e)
    return render_template('login.html')

def cancel_button_clicked():
    return render_template('login.html')

def is_valid_email(email):
    pat = re.compile(r'[\w.-]+@[\w.-]+.\w+')
    return re.match(pat, email) is not None

def check_matching_password(password, confirm_password):
    return password == confirm_password

# Run The App
if __name__ == '__main__':
    app.run(debug=True)