from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from .serializers import serialaizerpost,serializerCategory
from ...models import Post ,Category
from rest_framework.decorators import action
#from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView ,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
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


# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def apipost(request,id):
#     #try:
#         post= get_object_or_404(Post,id=id)
#         if request.method == "GET":
#             serializer = serialaizerpost(post)
#             serializer = serializer.data
#             return Response(serializer)
#         elif request.method == "PUT":
#             serializer = serialaizerpost(post,data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return  Response(serializer.data)
#         elif request.method == "DELETE":
#             post.delete()
#             return Response({"derail":"delet sucsessfully "},status=status.HTTP_204_NO_CONTENT)
#     #except:
#     #    return  Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def apilist(request):
#     if request.method =="GET":
#         post = Post.objects.all()
#         serialaizer = serialaizerpost(post,many=True)
#         return Response(serialaizer.data)
#     elif request.method == "POST":
#         serialaizer = serialaizerpost(data=request.data)
#         #if serialaizer.is_valid():
#         serialaizer.is_valid(raise_exception=True)
#         serialaizer.save()
#         return Response(serialaizer.data)
#         #else:
#         #     return Response(serialaizer.errors)

# class apilist (APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = serialaizerpost
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request):
#         post = Post.objects.all()
#         serialaizer = serialaizerpost(post,many=True)
#         return Response(serialaizer.data)
#     def post(self, request):
#         serialaizer = serialaizerpost(data=request.data)
#         serialaizer.is_valid(raise_exception=True)
#         serialaizer.save()
#         return Response(serialaizer.data)

# class apipost(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = serialaizerpost
#     """singel post and update post and deleted post"""
#     def get(self,request,id):
#         post= get_object_or_404(Post,id=id)
#         serializer = self.serializer_class(post)
#         serializer = serializer.data
#         return Response(serializer)
#     def put(self,request,id):
#         post= get_object_or_404(Post,id=id)
#         serializer = serialaizerpost(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return  Response(serializer.data)
#     def delete(self,request,id):
#         post= get_object_or_404(Post,id=id)
#         post.delete()
#         return Response({"derail":"delet sucsessfully "},status=status.HTTP_204_NO_CONTENT)


##genercview 
# class apilist(ListCreateAPIView):
#     """getting a lisi of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = serialaizerpost
#     queryset = Post.objects.filter(status=1)


class apipost(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serialaizerpost
    queryset = Post.objects.filter(status=1)


class apilist(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serialaizerpost
    queryset = Post.objects.filter(status=1)
    """
    A simple ViewSet for listing or retrieving users.
    """
    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset,many=True)
    #     return Response(serializer.data)
    # def retrieve(self, request, pk=None):
    #     queryset =get_object_or_404(self.queryset,pk=pk)
    #     serializer = self.serializer_class(queryset)
    #     return Response(serializer.data)
    # def create(self, request):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

"""
Category model
"""
class Categorymodelapi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializerCategory
    queryset = Category.objects.all()

    @action(methods=["get"],detail=False)
    def test_action(self,request):
        return Response({"ok":"test"}) 