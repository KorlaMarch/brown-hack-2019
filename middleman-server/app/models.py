from app import db

class HackSwitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    on = db.Column(db.Boolean)

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False
