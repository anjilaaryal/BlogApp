from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts, PostsComment
from posts.serializer import AddCommentRequest
from rest_framework.permissions import IsAuthenticated


class CreateCommentView(APIView):
    """" Adding new comments to the post"""
    permission_classes = [(IsAuthenticated)]


    def post(self, request, post_id):
        """" Add comment to a post """
        req_data = request.data
        user = request.user
        request_data = AddCommentRequest(data = req_data)
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        post_qs = UserPosts.objects.filter(id = post_id)
        if post_qs.exists():
            comment_qs = PostsComment.objects.create(posts = post_qs[0], comment = req_data["comment"], user = user)
            return Response({"id" : comment_qs.id, "comment" : comment_qs.comment}, status = 200)
        else:
            return Response({"msg" : "Please enter a valid Post Id"}, status=400)


    def get(self, request, post_id):
        """" Get comment from a post"""

        qs = PostsComment.objects.filter(posts_id = post_id)
        resp = []
        for comment in qs:
            resp.append({"id" : comment.id, "comment" : comment.comment, "user" : comment.user.email})
        return Response({"data" : resp}, status=200)