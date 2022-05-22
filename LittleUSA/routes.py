import email
from flask_login import login_required, current_user, login_user, logout_user
from LittleUSA.models import UserModel
from LittleUSA import app, db
from flask import render_template, redirect, request, url_for

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method== 'POST':
        email= request.form['email']
        user= UserModel.query.filter_by(email= email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods= ['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method== 'POST':
        email= request.form['email']
        username= request.form['username']
        password= request.form['password']

        if UserModel.query.filter_by(email=email).first():
            return ('Email already present')

        user= UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user) #add user into database, but this instruction just puts the user into database temporarily
        db.session.commit() #actually add the user into database
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/private-page')
def private_page():
    return render_template('private-page.html')