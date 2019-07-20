from flask import Flask, Blueprint, render_template, redirect, url_for
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
  return redirect(url_for('auth.login'))