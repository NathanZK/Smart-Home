from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Room
from . import db
import json

#import Adafruit_DHT



views = Blueprint('views', __name__)


@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("Home.html", user=current_user)

@views.route('/Rooms', methods=['GET'])
@login_required
def rooms():
    
    
    new_room = Room(name ="Living Room", temp=True, humid=True , lock = True, user_id=current_user.id)
    db.session.add(new_room)
    db.session.commit()
    return render_template("My-rooms.html", user=current_user)

@views.route('/Devices', methods=['GET', 'POST'])
@login_required
def devices():

    if request.method == 'POST':
        lock = request.form.get('lock')
        unlock = request.form.get('unlock')

    
    humidity, temperature = 35, 21 #Adafruit_DHT.read_retry(11,4)
    return render_template("My-Devices.html", user=current_user, humid = humidity, temp =temperature )

@views.route('/AddRoom', methods=['GET', 'POST'])
@login_required
def addroom():

    
    if request.method == 'POST':
        room = request.form.get('room')
        temp = request.form.get('temp')
        humid = request.form.get('humid')
        lock = request.form.get('lock')
        
        new_room = Room("Living Room", user_id=current_user.id)
        db.session.add(new_room)
        db.session.commit()

       
    return render_template("addroom.html", user=current_user )
