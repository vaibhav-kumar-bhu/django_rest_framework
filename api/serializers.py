from rest_framework import serializers
from api.models import student
class studentserial(serializers.Serializer):
	name=serializers.CharField(max_length=20)
	roll=serializers.IntegerField()
	age=serializers.IntegerField()
	state=serializers.CharField(max_length=20)

	def create(self,validate_data):
		return student.objects.create(**validate_data)
	def update(self,instance,validate_data):
		instance.name=validate_data.get('name',instance.name)
		instance.age=validate_data.get('age',instance.age)
		instance.roll=validate_data.get('roll',instance.roll)
		instance.state=validate_data.get('state',instance.state)
		instance.save()
		return instance



