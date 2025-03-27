from api4noobs import app
from helpers import UserForm
from flask import render_template, request, redirect, url_for, session, flash
from models import users
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    next_page = request.args.get('next')  # Captures the next page URL
    form = UserForm()
    return render_template('login.html', next=next_page,form=form)

@app.route('/auth', methods=['POST',]) # Checks if user exists in the 'users' dictionary
def auth():
    form = UserForm(request.form)
    user = users.query.filter_by(nickname=form.nickname.data).first()
    password = check_password_hash(user.password, form.password.data) # true or false

    if user and password: # Verifies if the user or password exists
        session['logged_in_user'] = user.nickname
        flash(f'User {user.nickname} successfully logged in!')
        next_page = request.form.get('next','')
        return redirect(next_page if next_page else url_for('index')) # Gets 'next' from <form>, with fallback to the homepage
    else: # If the user doesn't exist, it shows an error message
        flash('Incorrect password or user, try again!')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    # Removes the user from the session
    session.pop('logged_in_user', None)
    flash('Successfully logged out!')
    return redirect(url_for('index'))