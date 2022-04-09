from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

def home(request):
    return render(request, 'wpsr/home.html')

@api_view(['GET'])
def view_incident(request, pk):
    
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

@api_view(['POST'])
def update_incident(request, pk):
    
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "PUT":
        serializer = IncidentSerializer(incident, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_incident(request, pk):
    
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "DELETE":
        operation = incident.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
            return Response(data=data)
    
@api_view(['POST'])
def create_incident(request, pk):

    employee = Employee.objects.get(pk=pk) 
    
    report = Incident(employee_id=employee)
    
    if request.method == "POST":
        serializer = IncidentSerializer(report, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)