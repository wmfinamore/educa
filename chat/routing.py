from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    # Included method .as_asgi() , similar to Django .as_view()
    re_path(r'ws/chat/room/(?P<course_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
