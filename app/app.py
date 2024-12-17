from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for an event detail page
@app.route('/event/<event_id>')
def event(event_id):
    return render_template('event.html', event_id=event_id)

if __name__ == "__main__":
    app.run(debug=True)
