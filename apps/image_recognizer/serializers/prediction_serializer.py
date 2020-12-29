from rest_framework import serializers

from apps.image_recognizer.non_database_models import Prediction


class PredictionSerializer(serializers.Serializer):
    prediction = serializers.CharField()

    def create(self, validated_data):
        return Prediction(**validated_data)
