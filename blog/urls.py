from django.urls import path,include
from . import views
from django.conf.urls import url
from api.views import PostsUser

urlpatterns = [
    path('account/<user>/', views.stories, name='stories'),
    path('edit/', views.edit, name='edit'),
    path('register/', views.register),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()), 
    path('',views.main_page, name='main_page'),
    path('write_a_story/',views.write_a_story , name='write_a_story'),
    path("<category>/", views.blog_category, name="blog_category"),
    path('<slug:slug>', views.post, name='post'),
    path('<slug:slug>/comments/' , views.comments, name = 'comments'),
]