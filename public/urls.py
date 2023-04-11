from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello_world', views.hello_world, name='hello'),
    path('greet/<str:name>', views.greet, name='greet'),
    path('projects/<int:year>/<int:month>', views.projects, name='projects'),
]
