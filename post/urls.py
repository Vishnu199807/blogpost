from django.urls import path
from .views import user_registration, user_login, UserListView, PostCreateView,\
    comments_for_blog_post,blog_post_list, blog_post_detail,edit_or_delete_comment,delete_blog_post
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('register/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('postslist/', blog_post_list, name='blog_post_list'),
    path('posts/<int:pk>/', blog_post_detail, name='blog_post_detail'),
    path('posts/<int:blog_post_id>/comments/', comments_for_blog_post,name='comments_for_blog_post'),
    path('comments/<int:comment_id>/', edit_or_delete_comment, name='edit_or_delete_comment'),
    path('posts/<int:blog_post_id>/', delete_blog_post, name='delete_blog_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

