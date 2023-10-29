from django.urls import path
from . import views 


urlpatterns = [
    path("enroll/",views.enrolluser,name="enrolluser"),
    path("success/",views.success,name="success"),
]
