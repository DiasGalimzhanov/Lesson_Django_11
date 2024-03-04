from django.urls import path
from .views import home, comment

urlpatterns = [
    path("", home, name="home"),
    path("comment/<int:post_id>", comment, name="comment"),
]