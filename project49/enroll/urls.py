from django.urls import path 
from . import views 
urlpatterns = [
    path("student/<int:pk>",views.StudentDetailView.as_view(),name="studentdetail"),
    path("students/",views.StudentListView.as_view(),name="studentlist")
]
