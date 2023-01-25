from django.urls import path
from posts.views import CreatePostView, GetUpdatePostView, CreateCommentView

urlpatterns = [
    path('', CreatePostView.as_view()),
    path('<int:post_id>', GetUpdatePostView.as_view()),
    path('<int:post_id>/comment', CreateCommentView.as_view())

]