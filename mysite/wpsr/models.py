from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
                raise ValueError("Must provide Email.")
        if not password:
            raise ValueError('Must provide password.')
        
        Employee = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )
        
        Employee.set_password(password)
        Employee.save(using=self._db)
        return Employee
    
    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, **extra_fields )
    
    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, **extra_fields)

class Employee(AbstractBaseUser, PermissionsMixin): 
    # Abstractbaseuser has password, last_login, is_active by default
    
    email = models.EmailField(db_index=True, unique=True, max_length=250)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=20)
    #birth_date = models.DateTimeField('Birth-Date')
    
    is_staff = models.BooleanField(default=False) # supervisor
    is_active = models.BooleanField(default=True)   # authentication permission
    is_superuser = models.BooleanField(default=False) # true-> Admin, field inherit from PermissionsMIxin 
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Location(models.Model):
    building = models.CharField(max_length=100)
    room_num = models.IntegerField()

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Equipment(models.Model):
    serial_num = models.CharField(max_length=100)
    price = models.TextField(blank=True)

class UnsafeCondition(models.Model):
    description = models.TextField(blank=False)

class Incident(models.Model):
    empolyee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reported_date = models.DateField('reported-Date')
    incident_date = models.DateField('incident-Date')
    incident_time = models.TimeField('incident-Time')
    description = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    task_name = models.ForeignKey(Task, on_delete=models.CASCADE)
    injury_description = models.TextField(blank=True)
    first_aider = models.CharField(max_length=100)
    injury_nature = models.CharField(max_length=200)
    medical_needed = models.CharField(max_length=10)
    
class Investigation(models.Model):
    report_num = models.ForeignKey(Incident, on_delete=models.CASCADE)
    invest_date = models.DateField('invest-Date')
    incident_date = models.DateField('incident-Date')
    incident_time = models.TimeField('incident-Time')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    task_name = models.ForeignKey(Task, on_delete=models.CASCADE)  
    description = models.TextField(blank=True)
    prevent_suggest = models.TextField(blank=True)
 
class Timeclaim(models.Model):
    report_num = models.ForeignKey(Incident, on_delete=models.CASCADE)
    num_days = models.IntegerField()
    
class DamageClaim(models.Model):
    invest_id = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    cost = models.TextField(blank=True) 