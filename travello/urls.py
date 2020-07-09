from django.urls import  path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('description',views.description,name='description'),
    path('vbad',views.vbad,name='vbad'),
    path('bad',views.bad,name='bad'),
    path('mod',views.mod,name='mod'),
    path('good',views.good,name='good'),
    path('vgood',views.vgood,name='vgood'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('trending', views.trending, name='trending'),
    path('top', views.top, name='top'), 
    path('descriptiont',views.descriptiont,name='descriptiont'),
    path('descriptionto',views.descriptionto,name='descriptionto')
]