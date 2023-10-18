from django.urls import path, include
from . import views

app_name = "Food"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('item/', views.item, name='item'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    ## Add Items urls
    path('add/', views.CreateItem.as_view(), name="createItem"),
    ## Edit Items
    path('update/<int:id>/', views.updateItem, name="updateItem"),
    ## Delete Items
    path('delete/<int:id>/', views.deleteItem, name="deleteItem")
]