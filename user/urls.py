from django.urls import path
from user.views import HelloView, UserListView

urlpatterns = [
    path('hello/', HelloView.as_view()),
    path('user/', UserListView.as_view()),


]
