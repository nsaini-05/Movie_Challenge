from django.urls import path
from . import views
urlpatterns = [
  path("tickets", views.TicketList.as_view()),
  path("tickets/<int:pk>", views.TicketDetail.as_view())
]