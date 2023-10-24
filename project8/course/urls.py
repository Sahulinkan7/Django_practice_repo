from django.urls import path
from . import views


urlpatterns = [
    path("coursepage/",views.coursepage)
]
