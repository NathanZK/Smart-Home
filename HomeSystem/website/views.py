from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
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

@views.route('/Devices', methods=['GET'])
@login_required
def devices():
   # humidity, temperature = Adafruit_DHT.read_retry(11,4)
    return render_template("My-Devices.html", user=current_user )

