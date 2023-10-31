from django.urls import path, include
from .views import *

urlpatterns = [
    path('', acceptView, name='accept'),
    path('<int:id>/', resumeView, name='resume'),
    path('profiles/', listView, name='profilelist')
]