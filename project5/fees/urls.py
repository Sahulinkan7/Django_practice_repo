from django.urls import path
from . import views
urlpatterns = [
    path("coursefees/",views.course_fees),
]
