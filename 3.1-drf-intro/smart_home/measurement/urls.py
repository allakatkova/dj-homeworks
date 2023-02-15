from django.urls import path
from .views import CreateSensorView, ChangeSensorView, CreateMeasurementView, SensorDetailsView

urlpatterns = [
    path('sensors/create/', CreateSensorView.as_view()),
    path('sensors/change/<pk>/', ChangeSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('sensors/details/<pk>/', SensorDetailsView.as_view()),
]
