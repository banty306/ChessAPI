from django.urls import re_path, include
from django.urls import path
from chess.views.play_view import PlayView


urlpatterns = [
    re_path(r"^(?P<slug>[\w-]+)$", PlayView.as_view())


]
