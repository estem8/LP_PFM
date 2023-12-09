from flask import Flask, abort, render_template, session, redirect, url_for, request
from crud import create_user, user_list, last_news, create_news
import os

app = Flask(__name__)
app.secret_key= os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html',data = last_news())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['login'] == 'asd' and request.form['password'] == 'zxc':
        session['userLogged'] = request.form['login']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html',)

@app.route('/profile/<username>')
def profile(username):
    print(session)
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
        
    return f'Профиль {username}'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        create_user(login=username,password=password)
    return render_template('registration.html')

@app.route('/admin', methods=['GET', 'POST'])
def create_news_text():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        create_news(title=title,text=text)
    return render_template('admin_panel.html', data = last_news())

if __name__=='__main__':
    app.run(debug=True) 