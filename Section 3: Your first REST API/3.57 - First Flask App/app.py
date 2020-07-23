from flask import Flask

app = Flask(__name__)       # Created an object of Flask using a unique name


@app.route('/')  # 'http://www.google.com/'     - Created a Root
def home():  # Decorators always act on methods
    return "Hello, World!"


app.run(port=5000)
