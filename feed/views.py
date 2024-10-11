from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.
class HomepageView(ListView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-id")[0:30]
    
class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/new_post.html"
    fields = ["title", "text"]
