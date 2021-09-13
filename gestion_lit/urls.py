from django.urls import path

from gestion_lit import views


app_name ='gestion_lit'
urlpatterns = [
    path('departement/', views.departement_list,name='liste_dep'),
    path('departement/<int:id>/', views.departement_detail,name='detail_dep'),
]