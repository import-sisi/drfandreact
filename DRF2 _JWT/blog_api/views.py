from django.shortcuts import get_object_or_404
from yaml import serialize
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Display Posts

class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

# Post Search

class PostListDetailfilter(generics.ListAPIView):
  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']

# Post Admin

# class CreatePost(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class CreatePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
























# from turtle import title
# from rest_framework import generics
# from blog.models import Post
# from .serializers import PostSerializer
# from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
# from rest_framework import viewsets  # translate post and get request to create and list
# from rest_framework import filters
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response

# class PostUserWritePermission(BasePermission):
#     message = 'Editing posts is restricted to the author only.'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True

#         return obj.author == request.user

# class PostList(viewsets.ModelViewSet):  part 3
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
        
    

#     # Difine Custom Queryset
#     def get_queryset(self):
#         return Post.objects.all()

        

# class PostList(viewsets.ViewSet):  part 2
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrive(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk) # get singleoject from database
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

# class PostList(generics.ListCreateAPIView):   # part 1
#     permission_classes = [IsAuthenticated]
#     # queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(author=user)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    # permission_classes = [PostUserWritePermission]
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer

    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=item)


# class PostDetail(generics.RetrieveAPIView):
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         """
#         Feltering aganst the URL (ID)
#         get post based on title / string
#         """
#         slug = self.kwargs['pk']
#         print(slug)
#         return Post.objects.filter(slug=slug)


# class PostDetail(generics.ListAPIView):
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         slug = self.request.query_params.get('slug', None)
#         print(slug)
#         return Post.objects.filter(slug=slug)

# class PostListDetailfilter(generics.ListAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']

#     # '^' , '=' , '@' , '$'
    
#     def get_queryset(self):
#         slug = self.request.query_params.get('slug', None)
#         print(slug)
#         return super().get_queryset()


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
