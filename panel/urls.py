from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('list', views.list, name='list'),
    path('list/<int:id>', views.list_details, name='list-details'),
    path('list/<int:id>/update', views.update, name='update'),
    path('list/<int:id>/delete', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('incoming-call',  views.incoming_call,  name="incoming-call"),
    path('outer-call',  views.outer_call,  name="outer-call"),
    path('add-company',  views.add_company,  name="add-company"),
    path('list-company',  views.list_company, name= "list-company")




]
