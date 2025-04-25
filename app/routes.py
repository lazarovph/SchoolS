from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

main_routes = Blueprint('main_routes', __name__)
auth_routes = Blueprint('auth_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('home.html')

@auth_routes.route('/login')
def login():
    return render_template('login.html')

@auth_routes.route('/register')
def register():
    return render_template('register.html')
