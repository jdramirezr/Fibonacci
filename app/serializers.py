from rest_framework import serializers

class PascalSerializer(serializers.Serializer):
    rows = serializers.IntegerField()