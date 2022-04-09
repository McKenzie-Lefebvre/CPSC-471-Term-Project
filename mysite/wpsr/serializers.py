from rest_framework import serializers
from .models import *

# Used by the REST API

class CustomUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserManager
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = fields = '__all__'
    
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class UnsafeConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnsafeCondition
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
        
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
        
class InvestigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investigation
        fields = '__all__'
        
class TimeclaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeclaim
        fields = '__all__'
        
class DamageClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamageClaim
        fields = '__all__'