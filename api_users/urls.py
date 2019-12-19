from django.urls import path,include
from . import views
from django.conf.urls import url
from api.views import PostsUser,PostUser

urlpatterns = [
     path('posts/<user>/',PostsUser.as_view()),
     path('posts/<user>/<slug>/',PostUser.as_view()),
]