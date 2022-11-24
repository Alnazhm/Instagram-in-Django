from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from api.serializers import PostSerializer, CommentSerializer, LikeSerializer
from posts.models import Post, Comment, Like

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        elif request.method in ('PUT', 'PATCH', 'DELETE'):
            return obj.author == request.user
        elif request.user.is_authenticated and request.method == "POST":
            return True

class AddORDeleteLike(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in ("POST", 'DELETE'):
            return True

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,]


    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()


class LikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AddORDeleteLike,]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def delete(self, request, pk):
        print(pk)
        self.destroy()


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()
