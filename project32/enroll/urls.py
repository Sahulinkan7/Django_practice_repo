from django.urls import path 
from . import views 


urlpatterns = [
    path("",views.signup,name="signup"),
    path("login/",views.user_login,name="login"),
    path("profile/",views.profile_user,name="profile"),
    path("logout/",views.logout_user,name="logout"),
    path("passchange/",views.passwordchange,name="pwd"),
    path("setpass/",views.setnewpassword,name="setpass")
]
