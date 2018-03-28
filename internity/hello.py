from flask import Flask,redirect
import os

app = Flask(__name__)

portint = int(os.environ['PORT'])
@app.route('/')
def hello_world():
    return redirect("https://goo.gl/3UHty4", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=portint)
