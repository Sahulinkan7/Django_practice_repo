from django.urls import path 
from . import views 

urlpatterns = [
    path("enroll/<myid>/",views.home,name="home"),
    path("enroll/<myid>/<subid>/",views.home,name="home")
]
