from flask import render_template, request, redirect, url_for, session, flash
from api4noobs import app, db
from models import games
from helpers import GameForm

@app.route('/')
def index():
    # Just rendering home.html and showing the game list
    list = games.query.order_by(games.id)
    return render_template('list.html', title='Game', games=list)
@app.route('/new')
def new():
    # If the user isn't logged in, they’re blocked from accessing this page
    if 'logged_in_user' not in session or session['logged_in_user'] == None:
        return redirect(url_for('login', next=url_for('new')))  # Redirect with the next page
    form = GameForm()
    return render_template('new.html', title='New Game', form=form)  # Show new game page

@app.route('/create', methods=['POST'])  # Just creating a new game.
def create():
    form = GameForm(request.form)

    if not form.validate_on_submit(): # Verifies if the form is valid
        return redirect(url_for('new'))

    name = form.name.data
    category = form.category.data
    company = form.company.data

    game = games.query.filter_by(name=name).first()
    if game:# Verifies if the game already exists
        flash('Game already exists!')
        return redirect(url_for('new'))
    
    new_game = games(name=name, category=category, company=company)
    db.session.add(new_game) # Adds the new game to the database
    db.session.commit() # Commits the changes
    flash('Game created successfully!') # yay!

    return redirect(url_for('index'))  # Redirects to home

@app.route('/edit/<int:id>')
def edit(id):
    # If the user isn't logged in, they’re blocked from accessing this page
    if 'logged_in_user' not in session or session['logged_in_user'] == None:
        return redirect(url_for('login', next=url_for('edit', id=id)))  # Redirect with the next page
    game = games.query.filter_by(id=id).first()
    form = GameForm()
    form.name.data = game.name
    form.category.data = game.category
    form.company.data = game.company
    return render_template('edit.html', title='Editing Game', id=id,form=form)  # Show new game page

@app.route('/update', methods=['POST'])  # Just updating a game.
def update():
    form = GameForm(request.form)

    if form.validate_on_submit():
        
        game_id = request.form['id']
        game = games.query.filter_by(id=game_id).first()
        game.name = form.name.data
        game.category = form.category.data
        game.company = form.company.data

        db.session.add(game)
        db.session.commit() # Commits the changes
        flash('Game deleted successfully!')

    return redirect(url_for('index'))  # Redirects to game list(home)

@app.route('/delete/<int:id>')
def delete(id):
    # If the user isn't logged in, they’re blocked from accessing this page
    if 'logged_in_user' not in session or session['logged_in_user'] == None:
        return redirect(url_for('login', next=url_for('delete')))
    game = games.query.filter_by(id=id).first()
    db.session.delete(game)
    db.session.commit() # Commits the changes
    return redirect(url_for('index'))  # Redirects to game list(home)