from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('about/',views.aboutus, name='about'),
    path('contact/',views.contactus),
    path('count/',views.count, name='count')
]
