from flask import Flask, url_for
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route("/test", methods=['POST', 'GET'])
def test():
  if request.method == 'POST':
    return 'POST'
  else:
    return 'GET'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('show_user_profile', username='pipusana'))
    print(url_for('show_post', post_id=12))
    print(url_for('test'))


# FLASK_APP=router.py flask run --port 3002
# FLASK_APP=router.py flask run --host 127.0.0.0 --port 3002