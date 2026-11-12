from rest_framework import serializers
from ...models import Post

# class serialaizerpost(serializers.Serializer):
#     title = serializers.CharField(max_length=200)

class serialaizerpost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","content","author","status","category","image","pubished_date"]