from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("delete/<int:id>/",views.deletedata,name="deletestudent"),
    path("edit/<int:id>/",views.editdata,name="editstudent"),
]
