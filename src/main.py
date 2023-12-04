from flask import Flask, render_template
from flask import request
from crud import create_user
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',data = 'test_string')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        create_user(login=username,password=password)
    return render_template('registration.html')

if __name__=='__main__':
    app.run(debug=True)