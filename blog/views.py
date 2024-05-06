from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from .models import Post
from .forms import CommentForm
from django.views.generic import ListView
from django.views import View


class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(View):
    template_name = "blog/post-detail.html"

    def get_context_data(self, request, post):
        tags = post.tags.all()
        comment_form = CommentForm()
        comments = post.comments.all().order_by("-id")
        is_saved_for_later = str(post.id) in request.session.get("read_later", [])
        print("Is saved for later: ")
        print(is_saved_for_later)
        context = {
            "post": post,
            "tags": tags,
            "comment_form": comment_form,
            "comments": comments,
            "saved_for_later": is_saved_for_later,
        }
        return context

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = self.get_context_data(request, post)
        print(context)
        return render(request, self.template_name, context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())

        context = self.get_context_data(request, post)
        print(context)
        return render(request, self.template_name, context)


class ReadLaterView(View):
    def post(self, request):
        post_id = request.POST["post_id"]
        posts = request.session.get("read_later", [])
        if post_id not in posts:
            posts.append(post_id)
        else:
            posts.remove(post_id)
        request.session["read_later"] = list(set(posts))
        return HttpResponseRedirect("/posts/read-later")

    def get(self, request):
        post_ids = request.session.get("read_later", [])
        posts = Post.objects.filter(id__in=post_ids)
        return render(request, "blog/stored-posts.html", {"posts": posts})
