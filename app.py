from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
                         deploy_date=datetime.datetime.now().strftime("%B %d, %Y"))
@app.route('/test-favicon')
def test_favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)