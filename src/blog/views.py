from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from blog.models import BlogPost
from django.urls import reverse_lazy


class BlogHome(ListView):
    model = BlogPost
    template_name = "../templates/blogpost_list.html"
    context_object_name = "blog"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "../templates/blogpost_create.html"
    fields = ['title', 'content', ]


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "../templates/blogpost_edit.html"
    fields = ['title', 'content', 'published']
    success_url = reverse_lazy("blog:home")


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "../templates/blogpost_detail.html"
    context_object_name = "post"


class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    template_name = "../templates/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:home")
