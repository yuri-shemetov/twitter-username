from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView

from . import forms, models, services


class UsernamesFromTwitter(CreateView, ListView):
    form_class = forms.UsernameForm
    model = models.Username
    template_name = "twitter_usernames/index.html"

    def get_queryset(self):
        usernames = models.Username.objects.all()
        for username in usernames:
            username.followers = services.get_followers(username.username)
            username.following = services.get_following(username.username)
            username.description = services.get_description(username.username)
        return usernames

    def form_valid(self, form):
        form.data = form.data.copy()
        urls = form.data["username"].split("\n")
        for url in urls:
            if "https://twitter.com/" in url:
                words = url.split("https://twitter.com/")
                username = words[1]
                models.Username.objects.create(username=username)
        return redirect("/")


class UsernameTweets(DetailView):
    model = models.Username
    template_name = "twitter_usernames/tweets.html"

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context["tweets"] = services.get_10_tweets(self.object.username)
        return super().get_context_data(**context)
