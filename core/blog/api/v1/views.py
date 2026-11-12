from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from .serializers import serialaizerpost
from ...models import Post
data = {
    1:{
    "title":"blue"},
    2:{
    "title":"red"
    }
} 

@api_view()
def apiview(request):
    return Response({"ok":"gh"})


@api_view()
def apipost(request,id):
    #try:
        post= get_object_or_404(Post,id=id)
        serializer = serialaizerpost(post)
        serializer = serializer.data
        return Response(serializer)
    #except:
    #    return  Response(status=status.HTTP_404_NOT_FOUND)

@api_view()
def apilist(request):
      post = Post.objects.all()
      serialaizer = serialaizerpost(post,many=True)
      return Response(serialaizer.data)