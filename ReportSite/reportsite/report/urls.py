from django.urls import path, include
from .views import uploadView, helloView, reportView


urlpatterns = [
    path('', helloView, name='hello'),
    path('upload/', uploadView, name='upload'),
    path('report/', reportView, name='report')
]