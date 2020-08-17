from app.db import db, BaseModelMixin

class Diputy(db.Model, BaseModelMixin):

    __tablename__ = 'diputies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=True)
    birth_date = db.Column(db.Date(), nullable=True)
    dni = db.Column(db.String(20), nullable=True)
    sex = db.Column(db.Integer, nullable=False)
    db.UniqueConstraint(name, lastname)

    def __init__(self, name, lastname, birth_date, dni, sex):
        self.name = name
        self.lastname = lastname
        self.birth_date = birth_date
        self.dni = dni
        self.sex = sex

    def __repr__(self):
        return f'>Diputy({self.name})'

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_by_id(id):
        return Diputy.query.get(id)