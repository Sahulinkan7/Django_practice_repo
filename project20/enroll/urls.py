from django.urls import path
from . import views

urlpatterns = [
    path("enrollment/",views.enrollment,name="enrollment")
]
