from application import db, app

app.app_context().push()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    ability = db.Column(db.String(100), nullable=False)

    def __init__(self, name, type, ability):
        self.name = name
        self.type = type
        self.ability = ability

    def __repr__(self):
        return f"Pokemon is {self.name} and there type is {self.type}"
