from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('department/',views.department,name='department'),
    path('patient/',views.patient,name='patient'),
    path('contact/', views.contact, name='contact'),
]



