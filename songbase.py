from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    # return '<h1>hello world </h1>'
    return render_template('index.html')

@app.route('/songs')
def get_all_songs():
    songs = [
        'song 1',
        'song 2',
        'song 3'
    ]
    return render_template('songs.html',songs=songs)

@app.route('/user/<string:name>')
def get_user():
    #return '<h1>hello %s your age is %d/h1>' % (name, s)
    return render_template('user.html',user_name=name)
if __name__ == '__main__':
    """app.run(host='0.0.0.0',port=2000)"""
    app.run(debug=True)
