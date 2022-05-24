from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from .models import Room
#import Adafruit_DHT



views = Blueprint('views', __name__)


@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("Home.html", user=current_user)

@views.route('/Rooms', methods=['GET', 'POST'])
@login_required
def rooms():
    
    room = request.form.get('name')
    return render_template("My-rooms.html", user=current_user)

@views.route('/Devices', methods=['GET', 'POST'])
@login_required
def devices():
    
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    return render_template("My-Devices.html", user=current_user, humid = humidity, temp =temperature )

@views.route('/AddRoom', methods=['GET', 'POST'])
@login_required
def addroom():
    if request.method == 'POST':
        name = request.form.get('room')
        temp = request.form['temp']
        humid = request.form['humid']
        lock = request.form['lock']
        

        new_room = Room( name=name, temp = temp, humid = humid, lock =lock, user_id=current_user.id)
        db.session.add(new_room)
        db.session.commit()
        flash('Room added!', category='success')
    return render_template("addroom.html", user=current_user )
