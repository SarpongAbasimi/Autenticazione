from flask import Flask, Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  return render_template('login.html')

@auth.route('/signup')
def new():
  return render_template('signup.html')