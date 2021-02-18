from django.shortcuts import render
import io
from api.models import student
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from api.serializers import studentserial
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
	if request.method=='GET':
		json_string=request.body
		stream=io.BytesIO(json_string)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id',None)
		if id is not None:
			stu=student.objects.get(id=id)
			serializer=studentserial(stu)
			return JsonResponse(serializer.data,safe=False)
		else:
			stu=student.objects.all()
			serializer=studentserial(stu,many=True)
			return JsonResponse(serializer.data,safe=False)
	elif request.method=='POST':
		json_string=request.body
		stream=io.BytesIO(json_string)
		pythondata=JSONParser().parse(stream)
		serializer=studentserial(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			response={'msg':'data inserted successfully'}
			return JsonResponse(response,safe=False)
		else:
			response={'msg':'data cannot inserted'}
			return JsonResponse(response,safe=False)
	elif request.method=='PUT':
		json_string=request.body
		stream=io.BytesIO(json_string)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id')
		stu=student.objects.get(id=id)
		serializerss=studentserial(instance=stu,validate_data=pythondata,partial=True)
		if serializerss.is_valid():
			serializerss.save()
			res={'msg':'data updated'}
			return JsonResponse(res,safe=False)
	elif request.method=='DELETE':
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id')
		stu=student.objects.get(id=id)
		stu.delete()
		response={"msg":"Data deleted"}
		return JsonResponse(response,safe=False)

		

