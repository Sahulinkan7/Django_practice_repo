from django.urls import path 

from . import views 
urlpatterns = [
    path("",views.homelogin,name="home"),
    path("signup/",views.signupview,name="signup"),
    path("logout/",views.logoutuser,name="logout"),
    path("profile/<int:id>",views.profileuser,name="profile"),
    path("adminpage/",views.adminpage,name="adminpage")
]
