from flask import Flask, url_for, request, render_template, abort, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/test')
def test():
    abort(401)


@app.route('/why')
def why():
    return redirect(url_for('test'))


with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_world'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.debug = True
    app.run()
