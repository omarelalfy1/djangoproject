from django.urls import path
from .views import ListArticle, ListUser, DetailArticle,DetailUser

urlpatterns = [
    path("", ListArticle.as_view()),
    path("<int:pk>/", DetailArticle.as_view()),
    path("users/<int:pk>/", DetailUser.as_view()),
    path("users/", ListUser.as_view())
]
