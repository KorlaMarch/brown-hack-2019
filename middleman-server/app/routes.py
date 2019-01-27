from app import app, db
from flask import request
from app.models import HackSwitch


@app.route('/')
@app.route('/index')
def index():
    state = HackSwitch.query.get(1).on
    if state:
        return "on"
    else:
        return "off"

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
