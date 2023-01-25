from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.serializer import AddPostRequest
from posts.models import UserPosts
from rest_framework.permissions import IsAuthenticated


class GetUpdatePostView(APIView):
    """ Get, Update and Delete functionality of Posts from User"""
    permission_classes = [(IsAuthenticated)]


    def get(self, request, post_id):
        """ Get post from User"""
        user = request.user
        qs = UserPosts.objects.filter(id = post_id)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "title" : data.title, "description" : data.description, "created_at" : data.created_at})
        return Response({"data" : resp}, status=200)


    def put(self, request, post_id):
        """ Update Posts of User"""

        user = request.user
        post_qs = UserPosts.objects.filter(user = user, id = post_id)
        if post_qs.exists():
            title = request.data.get("title", None)
            description = request.data.get("description", None)
            if title:
                UserPosts.objects.filter(id = post_id).update(title = title)
            if description:
                UserPosts.objects.filter(id = post_id).update(description = description)
            return Response({"msg" : "Post Updated sucessfully"}, status=200)
        else:
            return Response({"msg" : "Access Denied"}, status=401)


    def delete(self, request, post_id):
        """Delete Posts"""

        user = request.user
        post_qs = UserPosts.objects.filter(user = user, id = post_id)
        if post_qs.exists():
            UserPosts.objects.filter(user = user, id = post_id).delete()
            return Response({"msg" : "Post Deleted Sucessfully"}, status=200)
        else:
            return Response({"msg" : "Access Denied"}, status=401)

