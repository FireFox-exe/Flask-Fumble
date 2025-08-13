from api4noobs import app
from extensions import db, bcrypt
from models import users, games

with app.app_context():
    
    db.create_all()

    if users.query.first() is None:

        user1 = users(nickname="Ayres", password=bcrypt.generate_password_hash("welcome").decode('utf-8'))

        user2 = users(nickname="ALC", password=bcrypt.generate_password_hash("hamsters").decode('utf-8'))

        user3 = users(nickname="JsS", password=bcrypt.generate_password_hash("password123").decode('utf-8'))

        db.session.add_all([user1, user2, user3])

        jogos = [
            games(name='Zelda', category='Adventure', company='Nintendo'),

            games(name='God of War', category='Hack n Slash', company='Sony'),
            games(name='Halo', category='FPS', company='Microsoft'),
            games(name='Metroid', category='Metroidvania', company='Nintendo'),

            games(name='Dark Souls', category='Souls', company='FromSoftware'),
            games(name='Red Dead Redemption', category='Action-Adventure', company='Rockstar'),
        ]

        db.session.add_all(jogos)
        db.session.commit()
        print(" Banco populado com sucesso.")
    else:
        print("Banco já contém dados. Nenhuma inserção feita.")
