from flask import request, Blueprint, jsonify
from random import randint
from core.models.users import User as user
from datetime import datetime

app = Blueprint('users', __name__)

# Author Sridhar V1.0 
# Create @ 2020.Jun.30 8:10 AM
# Useage : users conroller 


# http://127.0.0.1:5009/users/getall
@app.route('/getall', methods=['GET','POST'])
def getAll():
	# u = User()
	# temp = u.getAll()
	temp = user().getAll()
	print(temp)
	return jsonify(temp)

# http://127.0.0.1:5009/users/get
@app.route('/get', methods=['GET','POST'])
def get():
	user_id = request.values.get('user_id')
	print(request)
	temp = user().get(user_id)
	print(temp)
	return jsonify(temp)

# http://127.0.0.1:5009/users/create
@app.route('/create', methods=['GET','POST'])
def create():

	name  = "demo123"
	email = "demo123@demo.com"
	mobile = "1231231231"
	created_at = datetime.now()
	updated_at = datetime.now()
	data = {
		'name' : name,
		'email':email,
		'mobile':mobile,
		'created_at':created_at,
		'updated_at':updated_at
	}
	print(data)
	temp = user().create(data)
	print(temp)
	return jsonify(temp)

# http://127.0.0.1:5009/users/update
@app.route('/update', methods=['GET','POST'])
def update():

	user_id = 1
	name  = "demo123"
	email = "demo123@demo.com"
	mobile = "1231231231"
	created_at = datetime.now()
	updated_at = datetime.now()
	data = {
		'name' : name,
		'email':email,
		'mobile':mobile,
		'created_at':created_at,
		'updated_at':updated_at
	}
	print(data)
	temp = user().create(data)
	print(temp)
	return jsonify(temp)


