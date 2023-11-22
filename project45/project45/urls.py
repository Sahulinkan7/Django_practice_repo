"""
URL configuration for project45 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewfun/',views.funhome,name='funview'),
    path('viewclass/',views.Homeclassview.as_view(),name='classview'),
    path("formpage/",views.Homecontactview.as_view(),name="forms"),
    path("contextdata/",views.Home2View.as_view(),name="home2"),
    path("contextdata1/",views.Home3View.as_view(template_name='school/template1.html'),name="home3"),
     path("contextdata2/",views.Home3View.as_view(template_name='school/template2.html'),name="home3_1"),
]
