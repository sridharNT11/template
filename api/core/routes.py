from flask import request, Blueprint, jsonify
from core import app

# Author Sridhar V1.0 
# Create @ 2020.Jun.30 8:30 AM
# Useage : main route conroller

# Project default path 
@app.route('/', methods=['GET','POST'])
def index():
	return "my first test"	

# request.values: combined args and form, preferring args if keys overlap 
# https://stackoverflow.com/a/16664376
# Eg : http://127.0.0.1:5009/request_val 
@app.route('/request_val', methods=['GET','POST'])
def test():
	# if request.method == 'POST':
	# 	user_id = request.form.get('user_id')
	# else:
	# 	user_id = request.args.get('user_id')
	
	user_id = request.values.get("user_id")
	return jsonify(user_id)	

