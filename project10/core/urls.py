from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage),
    path("about/",views.aboutpage),
    path("courses/",views.coursepage)
]
