from flask import Flask, Blueprint, render_template, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
  return render_template('login.html')

@auth.route('/signup', methods=['GET'])
def new():
  return render_template('signup.html')

@auth.route('/sigup', methods=['POST'])
def create():
  return redirect(url_for('auth.login'))