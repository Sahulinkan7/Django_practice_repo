from django.urls import path 
from . import views 


urlpatterns = [
    path("",views.homelogin,name="home"),
    path("profile/",views.profileview,name="profile"),
    path("delete/<int:id>",views.deletedata,name="deletedata"),
    path("logout/",views.logoutuser,name="logout")
]
