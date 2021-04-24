from rest_framework.generics import CreateAPIView, ListAPIView
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer
from comment.models import Comment


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    # pagination_class = CommentPagination

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent=None)
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset = queryset.filter(post=query)
    #     return queryset
