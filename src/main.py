import time
from flask import Flask, abort, render_template, session, redirect, url_for, request
from sqlalchemy import select
from crud import create_user, last_news, create_news
from models import User
from db import Session
import os
from threading import Thread
from fake_generator import create_user_in_db, create_news

app = Flask(__name__)
app.secret_key= os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html',data = last_news())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login=request.form['login']
        password=request.form['password']
        with Session() as session:
            result = select(User).where(User.login==login, User.password)
            session.execute(result)
            print(result)
        
        # return redirect('/')
    return render_template('login.html')
    
    
    
    # if 'userLogged' in session:
    #     return redirect(url_for('profile', username=session['userLogged']))
    # elif request.method == 'POST' and request.form['login'] == 'asd' and request.form['password'] == 'zxc':
    #     session['userLogged'] = request.form['login']
    #     return redirect(url_for('profile', username=session['userLogged']))
    # return render_template('login.html',)

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

def add_random_item():
    while True:
        print('add new ')
        create_user_in_db(1)
        create_news(1)
        time.sleep(30)

thread = Thread(target=add_random_item)
thread.daemon=True
thread.start()

if __name__=='__main__':
    app.run(debug=True) 