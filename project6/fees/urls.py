from django.urls import path
from . import views

urlpatterns = [
    path("feesinfo/",views.feesinfo),
]
