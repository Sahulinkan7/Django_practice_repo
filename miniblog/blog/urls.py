from django.urls import path
from . import views 


urlpatterns = [
    path("",views.homeview,name="home"),
    path("dashboard/",views.dashboardview,name="dashboard"),
    path("newblog/",views.writeblogview,name="newblog"),
    path("editpost/<int:id>/",views.updatepost,name="editpost"),
    path("deletepost/<int:id>/",views.deletepost,name="deletepost")
]
