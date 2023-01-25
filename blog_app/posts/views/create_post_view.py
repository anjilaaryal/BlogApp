from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.serializer import AddPostRequest
from posts.models import UserPosts
from rest_framework.permissions import IsAuthenticated


class CreatePostView(APIView):
    """Adding new Posts"""
    permission_classes = [(IsAuthenticated)]


    def post(self, request):
        """Adding New Posts"""
        user = request.user
        req_data = request.data
        request_data = AddPostRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        qs = UserPosts.objects.create(title = req_data["title"], description = req_data["description"], user = user)
        print(qs)
        return Response({"id": qs.id , "title": qs.title , "description": qs.description}, status = 201)


    def get(self, request):
        """ Get Post from user"""
        user = request.user
        qs = UserPosts.objects.filter(user = user)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "title" : data.title, "description" : data.description, "created_at" : data.created_at})
        return Response({"data" : resp}, status=200)
