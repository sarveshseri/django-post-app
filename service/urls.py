from django.urls import path
from django.urls import include

urlpatterns = [
    path("api/v1/posts/", include("posts.urls"))
]
