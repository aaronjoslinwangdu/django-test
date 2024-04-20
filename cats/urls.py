from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllCats.as_view(), name='index'),
    path("yvonne", views.YvonneCats.as_view(), name='yvonne')
]

