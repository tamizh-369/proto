from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing():
    return "Hello World: Ambulance Dispatch Pipeline Active"

if __name__ == '__main__':
    app.run(debug=True)