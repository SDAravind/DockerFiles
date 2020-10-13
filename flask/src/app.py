from flask import Flask
import random, string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, welcome to Flask Application!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')