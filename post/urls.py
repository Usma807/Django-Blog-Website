from django.urls import path # type: ignore
from .views import PostsShow,PostOpen
urlpatterns = [
    path('', PostsShow.as_view(), name='home'),
    path('posts/<int:pk>', PostOpen.as_view(), name='post_detail')
]
