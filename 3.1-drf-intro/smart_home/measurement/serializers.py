from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(
        source='sensor', read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'description', 'measurements']
