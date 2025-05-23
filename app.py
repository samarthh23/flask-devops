from flask import Flask, render_template
import requests  # For API calls

app = Flask(__name__)

# Sample API data (replace with real API later)
tech_stack = [
    {"name": "Python", "icon": "🐍", "category": "Backend"},
    {"name": "Flask", "icon": "🚀", "category": "Framework"},
    {"name": "Render", "icon": "☁️", "category": "Cloud"}
]

@app.route('/')
def home():
    return render_template('index.html', tech=tech_stack)

@app.route('/api-demo')
def api_demo():
    # Example: Fetch random user data
    response = requests.get('https://randomuser.me/api/')
    user_data = response.json()['results'][0]
    return render_template('api_demo.html', user=user_data)