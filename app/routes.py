from flask import Flask, render_template, request, redirect, url_for, Blueprint

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/login')
def login():
    return render_template('login.html')

@main_routes.route('/logout')
def logout():
    return redirect(url_for('login'))

@main_routes.route('/register')
def register():
    return render_template('register.html')

@main_routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


