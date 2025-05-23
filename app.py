from flask import Flask, render_template
import requests  # For API calls
import os  # For environment variables

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
    try:
        # Example: Fetch random user data with timeout
        response = requests.get('https://randomuser.me/api/', timeout=5)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        user_data = response.json()['results'][0]
        return render_template('api_demo.html', user=user_data)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e)), 500

# Get port from environment variable or use default 5000
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)