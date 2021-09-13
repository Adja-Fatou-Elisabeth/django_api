from django.db.models import fields
from rest_framework import serializers
from gestion_lit.models import *


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('__all__')