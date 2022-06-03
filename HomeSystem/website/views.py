from flask import Blueprint, render_template, request, flash, jsonify
import flask
from flask import session, url_for
from flask_login import login_required, current_user
from .models import Room
from . import db
import json

#import Adafruit_DHT
# import RPi.GPIO as GPIO






views = Blueprint('views', __name__)


@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("Home.html", user=current_user)

@views.route('/Rooms/', methods=['GET','POST'])
@login_required
def rooms():
    if request.method == 'GET':
        return render_template("My-rooms.html", user=current_user)
    if request.method == 'POST':
        name= request.form["room_button"]
        
        return flask.redirect(url_for('.devices', name=name))
    

@views.route('/Devices/<name>', methods=['GET', 'POST'])
@login_required

def devices(name):
    # from gpiozero import Servo
    # from time import sleep
    # myGPIO = 25
    # myCorrection = 0.45
    # maxPW = (2.0 + myCorrection) / 1000
    # minPW = (1.0 - myCorrection) / 1000
    # servo = Servo(myGPIO, min_pulse_width = minPW, max_pulse_width=maxPW)

    

    room= Room.query.filter_by(name=name).first()
    str = room.lockstatus
    
    doorstatus =""
    if request.method == 'POST':
        if request.form['submit_button'] == 'Lock':
            room.lockstatus= "Locked"
            str = room.lockstatus
            # servo.min()
            # servo.min()
            # sleep(1)
        elif request.form['submit_button'] == 'Unlock':
            room.lockstatus="Unlocked"
            str = room.lockstatus
            # servo.max()
            # sleep(1)
   

        # GPIO.setmode(GPIO.BOARD)

        # GPIO.setup(11,GPIO.OUT)
        # GPIO.output(11,1)
        # GPIO.setup(13,GPIO.OUT)
        # GPIO.output(13,1)
        # GPIO.setup(15,GPIO.OUT)
        # GPIO.output(15,1)

        # hex = request.form.get('rgb').lstrip('#')
        # rgbValue =  tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        
        # if rgbValue[0] <125:
        #     red = 0
        # else:
        #     red = 1
 
        # if rgbValue[1] <125:
        #     green = 0
        # else:
        #     green = 1

        # if rgbValue[2] <125:
        #     blue = 0
        # else:
        #     blue = 1

              
        # GPIO.output(11,int(red))
        # GPIO.output(13,int(green))
        # GPIO.output(15,int(blue))
        
       
    db.session.commit()       
    if str =="Locked":
        doorstatus = "Unlock"
    elif str=="Unlocked":
        doorstatus ="Lock"
    
    humidity, temperature = 35, 21 #Adafruit_DHT.read_retry(11,4)
    return render_template("My-Devices.html", user=current_user, humid = humidity, temp =temperature, str=str, doorstatus = doorstatus, room=room )

@views.route('/AddRoom', methods=['GET', 'POST'])
@login_required
def addroom():

    if request.method == 'GET':
        return render_template("addroom.html", user=current_user )

    if request.method == 'POST':
        room = request.form['room']
       
        temp=False
        humid=False
        lock=False
        led=False
        if  request.form.get('temp'):
            temp=True
    
        if  request.form.get('humid'):
            humid=True
       
        if  request.form.get('lock'):
            lock=True
       
        if  request.form.get('led'):
            led=True
    
        new_room = Room(name =room, temp= temp, humid =humid, lock =lock, lockstatus="Locked", led =led, user_id=current_user.id)
        db.session.add(new_room)
        db.session.commit()
        
        return flask.redirect("/Rooms")
        

        
       
    
