from django.urls import path
from . import views

urlpatterns = [
#main page url
    path('',views.mainview,name='index'),
    #second page url
    path('Second/<int:pk>/',views.Secondview.as_view(),name='second'),
    path('about/',views.Aboutview,name='about'),
    path('contect/',views.contectview,name='contect'),
]
