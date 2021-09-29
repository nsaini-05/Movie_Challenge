from django.urls import path
from . import views 

urlpatterns = [
  path("shows", views.ShowList.as_view()),
  path("shows/<int:pk>", views.ShowDetail.as_view())
]