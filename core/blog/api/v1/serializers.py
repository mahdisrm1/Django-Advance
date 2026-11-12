from rest_framework import serializers

class serialaizerpost(serializers.Serializer):
    title = serializers.CharField(max_length=200)