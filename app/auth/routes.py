from app import db
from app.models import User
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from .form import SignUpForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
  loginform = LoginForm()
  return render_template('login.html', loginform=loginform)

@auth.route('/session', methods=['POST'])
def new_session():
  loginform = LoginForm()
  if request.method == 'POST' and loginform.validate_on_submit():
    user = User.query.filter_by(email= loginform.email.data).first()
    if user and user.check_password(loginform.password.data):
      login_user(user)
      next = request.args.get('next')
      return redirect(url_for('main.index')) if next is None else redirect(url_for(next))
    flash('Invalid email or password.')
  return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET'])
def new():
  sign_up_form = SignUpForm()
  return render_template('signup.html', form=sign_up_form)

@auth.route('/signup', methods=['POST'])
def create():
  sign_up_form = SignUpForm()
  if request.method == 'POST' and sign_up_form.validate_on_submit():
    if sign_up_form.password.data == sign_up_form.confirm_password.data:
      user = User(name=sign_up_form.name.data, email=sign_up_form.email.data)
      user.set_password(sign_up_form.password.data)
      db.session.add(user)
      db.session.commit()
      flash('You were successfully registered.')
      return redirect(url_for('auth.login'))
    flash('Invalid username or password.')
  return render_template('signup.html', form=sign_up_form)
  