from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status 

from gestion_lit.models import *
from gestion_lit.serializers import *
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def departement_list(request):
    if request.method == 'GET':
        departements = Departement.objects.all()
        nom_departement = request.GET.get('nom_dep', None)
        if nom_departement is not None:
            departements = departements.filter(nom_dep__icontains = nom_departement)
        departements_serializers  = DepartementSerializer(departements,many=True)
        return JsonResponse(departements_serializers.data, safe=False)
    elif request.method == 'POST':
        departement_data = JSONParser().parse(request)
        departement_serializer = DepartementSerializer(data=departement_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse(departement_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(departement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Departement.objects.all().delete()
        return JsonResponse({'message': '{} Departement supprime'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def departement_detail(request,id):
    try:
        departement = Departement.objects.get(id = id)
        if request.method == 'GET':
            departement_serializer = DepartementSerializer(departement)
            return JsonResponse(departement_serializer.data)
        elif request.method == 'PUT': 
            departement_data = JSONParser().parse(request) 
            departement_serializer = DepartementSerializer(departement, data=departement_data) 
            if departement_serializer.is_valid(): 
                departement_serializer.save() 
                return JsonResponse(departement_serializer.data) 
            return JsonResponse(departement_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            departement.delete() 
            return JsonResponse({'message': 'Departement supprimé'}, status=status.HTTP_204_NO_CONTENT)
    except Departement.DoesNotExist:
        return JsonResponse({'message' : 'Le departement n\'esxiste pas'}, status =status.HTTP_404_NOT_FOUND)
