from django.urls import path
from . import views
urlpatterns = [
    path('posts/',  views.PostList.as_view()),
    path('posts/<slug>/',views.PostOne.as_view()),

]