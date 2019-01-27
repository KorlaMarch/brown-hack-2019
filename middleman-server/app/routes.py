from app import app, db
from flask import request
from app.models import HackSwitch


@app.route('/')
@app.route('/index')
def index():
    res = ""
    switch = HackSwitch.query.get(1)
    if switch.on:
        res += "on"
    else:
        res += "off"
    res += " " + str(switch.angle_x)
    res += " " + str(switch.angle_y)
    return res

@app.route('/on')
def on():
    switch = HackSwitch.query.get(1)
    switch.on = True
    db.session.commit()
    return "ok"

@app.route('/off')
def off():
    switch = HackSwitch.query.get(1)
    switch.on = False
    db.session.commit()
    return "ok"

@app.route('/submit')
def angle():
    switch = HackSwitch.query.get(1)
    switch.angle_x = float(request.args.get('anglex'))
    switch.angle_y = float(request.args.get('angley'))
    db.session.commit()
    return "ok"
