from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Location)
admin.site.register(UnsafeCondition)
admin.site.register(Equipment)
admin.site.register(Incident)
admin.site.register(Investigation)
admin.site.register(Timeclaim)
admin.site.register(DamageClaim)