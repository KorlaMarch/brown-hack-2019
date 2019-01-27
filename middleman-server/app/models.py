from app import db

class HackSwitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    on = db.Column(db.Boolean)
    angle_x = db.Column(db.Float)
    angle_y = db.Column(db.Float)

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def set_angle(self, angle_x, angle_y):
        self.angle_x = angle_x
        self.angle_y = angle_y
