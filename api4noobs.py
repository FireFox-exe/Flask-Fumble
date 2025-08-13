from flask import Flask
from extensions import db, csrf, bcrypt

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db.init_app(app)
csrf.init_app(app)
bcrypt.init_app(app)

from users_views import *

from game_views import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)