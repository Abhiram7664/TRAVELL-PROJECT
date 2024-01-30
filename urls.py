from . import views
from django.urls import path

urlpatterns = [

    path('',views.past,name='past')
]