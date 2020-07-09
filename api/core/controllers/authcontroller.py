from flask import request, Blueprint, jsonify
from random import randint
import datetime

app = Blueprint('auth', __name__)

# Author Sridhar V1.0 
# Create @ 2020.Jun.30 8:30 AM
# Useage : auth route conroller 


@app.route('/login', methods=['GET','POST'])
def login():
	return "Users login"
