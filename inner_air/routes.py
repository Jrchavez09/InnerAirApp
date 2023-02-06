from inner_air import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required

from inner_air.forms import RegisterForm, LoginForm
from inner_air.models import Exercise, User, Routine, Favorites, Statistics, Category, UserRating


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(password=form.password.data):
            login_user(user)
            flash(f'Success! You are logged in as: {user.firstname}', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash('You have entered an invalid email address or password.', category='danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        Return the register.html page
    """
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(
            firstname=form.firstname.data,
            email=form.email.data,
            hashed_password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'Account created successfully for {new_user.firstname}', category='success')
        return redirect(url_for('login'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
        I tried to create a table so that something can be displayed, nothing fancy.
    """
    users = User.query.all()
    exercises = Exercise.query.all()
    return render_template('dashboard.html',users=users, exercises=exercises)



@app.route('/logout')
def logout():
    logout_user()
    flash('you\'ve been logged out', category='info')
    return redirect(url_for('home'))
