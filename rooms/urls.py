from django.urls import path
from . import views
urlpatterns = [
  path("rooms", views.RoomList.as_view()),
  path("rooms/<int:pk>", views.RoomDetail.as_view())
]