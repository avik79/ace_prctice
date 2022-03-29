from flask import Flask

app = Flask(__name__)

@app.route('/')
def demo():
    return 'Demo Service - V1'
