import requests
import json

URL="http://127.0.0.1:8000/"

def get_data(id=None):
	data={}
	if id is not None:
		data={'id':id}
	json_string=json.dumps(data)
	response=requests.get(url=URL ,data=json_string)
	print(response.json())

#get_data()

def create_data():
	data={
	'name':'vaibhav',
	'roll': 20,
	'age':30,
	'state':'uttar pradesh'

	}
	json_string=json.dumps(data)
	response=requests.post(url=URL,data=json_string)
	print(response.json())
#create_data()

def update_data():
	data={
	'id':5,
	'name':'vks',
	'age':45,
	'state':'uttar pradesh',
	
	}
	json_data=json.dumps(data)
	response=requests.put(url=URL,data=json_data)
	print(response.json())

#update_data()

def delete_data():
	data={
	'id':4
	
	}
	json_data=json.dumps(data)
	response=requests.delete(url=URL,data=json_data)
	print(response.json())

delete_data()


