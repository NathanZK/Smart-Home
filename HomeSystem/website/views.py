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
    
    return render_template("My-rooms.html", user=current_user)

@views.route('/Devices', methods=['GET', 'POST'])
@login_required

def devices():
    # from gpiozero import Servo
    # from time import sleep
    # myGPIO = 25
    # myCorrection = 0.45
    # maxPW = (2.0 + myCorrection) / 1000
    # minPW = (1.0 - myCorrection) / 1000
    # servo = Servo(myGPIO, min_pulse_width = minPW, max_pulse_width=maxPW)


    str= "Locked"
    if request.method == 'POST':
        if request.form['submit_button'] == 'Lock':
            str= "Locked"
            # servo.min()
            # servo.min()
            # sleep(1)
        elif request.form['submit_button'] == 'Unlock':
            str="Unlocked"
            # servo.max()
            # sleep(1)
            
    humidity, temperature = 35, 21 #Adafruit_DHT.read_retry(11,4)
    return render_template("My-Devices.html", user=current_user, humid = humidity, temp =temperature, str=str )

@views.route('/AddRoom', methods=['GET', 'POST'])
@login_required
def addroom():

    if request.method == 'GET':
        return render_template("addroom.html", user=current_user )

    if request.method == 'POST':
        room = request.form['room']
        temp = request.form['temp']
        humid = request.form['humid']
        lock = request.form['lock']
        
        new_room = Room(name =room, user_id=current_user.id)
        db.session.add(new_room)
        db.session.commit()
        
        return render_template("My-rooms.html", user=current_user)

        
       
    
