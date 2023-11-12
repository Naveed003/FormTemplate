from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('homeButtons',views.mainButtonHandling,name="homeButtons"),
    path('authenticate',views.Login,name='Login'),
    path('FileSave',views.filesave,name='FileSave'),
    path('fill',views.fill,name='fill'),
]
