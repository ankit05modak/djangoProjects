from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RegularTypeViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(typ="Regular")
    serializer_class = StudentSerializer

class ActiveTypeViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(typ="Active")
    serializer_class = StudentSerializer