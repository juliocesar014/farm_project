from rest_framework import serializers
from farm.models import Owner, Farm


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'name', 'document', 'document_type', 'creation_date', 'last_modification_date', 'is_active']
        
        
        
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'name', 'geometry', 'area', 'centro_id', 'creation_date', 'last_modification_date', 'is_active', 'municipio', 'estado', 'owner']
        
        
        
class ListFarmOwnerSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    class Meta:
        model = Farm
        fields = ['id', 'name', 'geometry', 'area', 'centro_id', 'creation_date', 'last_modification_date', 'is_active', 'municipio', 'estado', 'owner']