from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Post,Comment,Profile,Category
from .forms import CommentForm,PostForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import LoginForm, UserRegistrationForm
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def write_a_story(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.published_date = timezone.now()
            post.save()
            return redirect('post', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'write_story.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

@login_required
def stories(request, user):
    usr = int(user)-1
    posts = Post.objects.filter(user=str(usr)).order_by('-created_on')
    context ={
        'posts':posts,
    }
    return render(request,'stories.html',context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(".")
        else:
            return HttpResponseRedirect('.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

# Create your views here.


def main_page(request):
    posts = Post.objects.all().order_by('-created_on')
    categories = Category.objects.all()
    context = {
          "posts": posts,
          'categories':categories
    }
    return render(request, "main_page.html", context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
          "post": post,
          'categories':categories
    }
    return render(request, "post.html", context)

def comments(request,slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect('/{}/comments/'.format(slug))
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {
          "post": post,
          "comments": comments,
          "form": form,
          'categories':categories
    }
    return render(request, "comments.html", context)

def blog_category(request, category):
    categories = Category.objects.all()
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts,
        'categories':categories
    }
    return render(request, "blog_category.html", context)

# def write_a_story(request):
#     return render(request, 'write_story.html')
# def user_profile(request, username, slug):
#     user = User.objects.filter(username = username)
#     print(user)
#     context={
#         'user':user
#     }
#     return render(request, 'user_profile.html',context)

