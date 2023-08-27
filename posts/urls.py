from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_post),
    path("<uuid:id>/analysis", views.get_post_analysis),
]
