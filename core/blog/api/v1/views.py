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


@api_view(["GET","PUT","DELETE"])
def apipost(request,id):
    #try:
        post= get_object_or_404(Post,id=id)
        if request.method == "GET":
            serializer = serialaizerpost(post)
            serializer = serializer.data
            return Response(serializer)
        elif request.method == "PUT":
            serializer = serialaizerpost(post,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return  Response(serializer.data)
        elif request.method == "DELETE":
            post.delete()
            return Response({"derail":"delet sucsessfully "},status=status.HTTP_204_NO_CONTENT)
    #except:
    #    return  Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET","POST"])
def apilist(request):
    if request.method =="GET":
        post = Post.objects.all()
        serialaizer = serialaizerpost(post,many=True)
        return Response(serialaizer.data)
    elif request.method == "POST":
        serialaizer = serialaizerpost(data=request.data)
        #if serialaizer.is_valid():
        serialaizer = serialaizer.is_valid(raise_exception=True)
        serialaizer.save()
        return Response(serialaizer.data)
        #else:
        #     return Response(serialaizer.errors)