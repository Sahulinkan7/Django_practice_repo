from django.urls import path 
from . import views 


urlpatterns = [
    path("",views.homelogin,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout_user,name="logout"),
    path("profile/",views.user_profile,name="profile"),
    path("changepass/",views.changepass,name="changepass"),
    path("setpass/",views.setnewpass,name="setpass")
]
