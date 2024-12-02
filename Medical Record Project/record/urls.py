from django.urls import path
from .views import PatientListView, PatientDetailView, PatientUpdateView, PatientDeleteView, PatientCreateView
urlpatterns = [
    path("patient/new/", PatientCreateView.as_view(), name="patient_new"),
    path("patient/<int:pk>/delete", PatientDeleteView.as_view(), name="patient_delete"),
    path("patient/<int:pk>/edit", PatientUpdateView.as_view(), name="patient_edit"),
    path("detail/<int:pk>/", PatientDetailView.as_view(), name="patient_detail"),
    path("", PatientListView.as_view(), name="patient_list"),
    
]
