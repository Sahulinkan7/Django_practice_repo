from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.Addshowview.as_view(),name="addshow"),
    path("deleteview/<int:id>",views.DeleteView.as_view(),name='delete'),
    path("updateview/<int:id>",views.Updateview.as_view(),name='update')
]
