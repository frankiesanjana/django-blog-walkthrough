from . import views
from django.urls import path

# the first slug in angle  brackets is called a path converter. The second slug is a keyword name.
    # The path converter converts this text into a slug field, it tells Django to match any slug string, which consists of ASCII characters or numbers  plus the hyphen and underscore characters.
    # the 'slug' keyword name matches the 'slug' parameter in the 'get' method of the PostDetail class in the blog/view.py file and is how we link them together
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]