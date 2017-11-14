from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = 'this should be a secret key'


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/courses')
def show_all_courses():
    courses = [
        ['MISY350:Business Application Development II','You will learn a wide range of client-side and server-side technologies.'],
        ['MISY430:Systems Analysis & Implementation', 'You will learn how to analyze business problems an provide IT solutions.'],
        ['MISY380:ERP Systems','You will learn SAP.']
    ]

    return render_template('courses-all.html', courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/users')
def show_all_users():
    return render_template('user-all.html')


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    # how to get form data is different for GET vs. POST
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        return render_template('form-demo.html', first_name=first_name)
    if request.method == 'POST':
        first_name = request.form['first_name']
        return render_template('form-demo.html', first_name=first_name)


@app.route('/user/<string:name>/')
def get_user_name(name):
    # return "hello " + name
    # return "Hello %s, this is %s" % (name, 'administrator')
    return render_template('user.html', name=name)


@app.route('/song/<int:id>/')
def get_song_id(id):
    # return "This song's ID is " + str(id)
    return "Hi, this is %s and the song's id is %d" % ('administrator', id)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
