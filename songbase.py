from flask import Flask
app = Flask(__name__)


@app.route('/user/<string:name>')
def get_user():
    return '<h1>hello %s your age is %d/h1>' % (name, s)
if __name__ == '__main__':
    """app.run(host='0.0.0.0',port=2000)"""
    app.run(debug=True)
