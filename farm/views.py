from rest_framework import viewsets, generics
from farm.models import Owner, Farm
from farm.serializer import OwnerSerializer, FarmSerializer, ListFarmOwnerSerializer


class OwnersViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    
    

class FarmsViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    
    
class ListFarmOwnerList(generics.ListAPIView):
    # List Farm for a specific owner
    def get_queryset(self):
        queryset = Farm.objects.filter(owner_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListFarmOwnerSerializer