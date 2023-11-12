from django.urls import path
from . import views

app_name = "measurements"
urlpatterns = [
    path("", views.list, name="list"),
    path("<int:id>", views.details, name="details"),

]