from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body"
    )
    template_name = "article_edit.html"
    login_url = "login"



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    login_url = "login"




class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body",)
    login_url = "login"

    def from_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
