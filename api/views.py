from django.shortcuts import render
from rest_framework import viewsets
from api.models import Employee,Company
from api.serializers import EmployeeSerializer,CompanySerializer

# Create your CompanyViewset views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
# Create your EmployeeViewset views here.
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
