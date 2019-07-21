from app import db
from app.models import User
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from .form import SignUpForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
  return render_template('login.html')

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
  return render_template('signup.html', form=sign_up_form )
  