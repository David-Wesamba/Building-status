from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name = 'home'),
    path('init/<int:pk>/',views.view, name = 'view'),
    path('b-status/',views.status, name = 'status'),
    path('about/',views.about, name = 'about'),
]