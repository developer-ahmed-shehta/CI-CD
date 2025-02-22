from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, CI/CD World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
