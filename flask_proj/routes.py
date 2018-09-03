from flask import render_template, redirect, url_for, request, flash
from flask_proj.forms import RegistrationForm, LoginForm
#Model for DB
from flask_proj.models import User
from flask_proj import app
from flask_proj import db

#Post data to DB
@app.route('/post_user',methods=['POST'])
def post_user():
    user = User(request.form['username'],request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))

#Query by name
@app.route('/user/<x>')
def show_user(x):
    item = User.query.filter_by(name = x).first()
    return render_template('show_user.html',item=item)


@app.route("/")
@app.route("/home")
def home():
    all_users = User.query.all()
    return render_template('home.html',all_users=all_users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '1234':
            return redirect('loggedin')
    return render_template('login.html', title= 'Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title= 'Register', form=form)

@app.route("/newuser")
def newuser():
    return render_template('newuser.html')

@app.route("/loggedin",methods=['GET', 'POST'])
def loggedin():
    return render_template('loggedin.html')
