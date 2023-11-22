from django.urls import path 
from . import views

urlpatterns = [
    path("",views.Mylistview.as_view(),name="listview")
]
