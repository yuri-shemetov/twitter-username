from django.urls import path
from . import views


urlpatterns = [
    # Main
    path("", views.UsernamesFromTwitter.as_view(), name="usernames"),
    path("<int:pk>/", views.UsernameTweets.as_view(), name="username_tweets"),
]
