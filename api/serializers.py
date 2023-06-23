from rest_framework import serializers
from api.models import Employee,Company

# create Company serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    Company_id=serializers.ReadOnlyField()
    class Meta :
        model=Company
        fields="__all__"
# create EMployee serializers

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id=serializers.ReadOnlyField()
    class Meta :
        model=Employee
        fields="__all__"
