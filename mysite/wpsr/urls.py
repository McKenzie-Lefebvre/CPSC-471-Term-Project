from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name='WPSR-home'),
    path('<pk>/', view_incident, name='incident_view'),
    path('<pk>/update/', update_incident, name='incident_update'),
    path('<pk>/delete/', delete_incident, name='incident_delete'),
    path('<pk>/delete/', create_incident, name='incident_create'),
]   
