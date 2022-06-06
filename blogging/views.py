from blogging.models import Post, Category
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets, permissions
from blogging.serializers import UserSerializer, PostSerializer, CategorySerializer

from django.shortcuts import render, redirect
from django.utils import timezone
from blogging.forms import add_post

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# from mysite import settings


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@login_required
def add_model(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    if request.method == "POST":
        form = add_post(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.published_date = timezone.now()
            model_instance.save()
            return redirect("/")

    else:
        form = add_post()

        return render(request, "blogging/add.html", {"form": form})
