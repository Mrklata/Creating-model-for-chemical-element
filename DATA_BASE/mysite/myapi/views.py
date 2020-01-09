from rest_framework import viewsets
from .serializers import ChemSerializer
from .models import Chem


class ChemViewSet(viewsets.ModelViewSet):
    queryset = Chem.objects.all().order_by('atomic_number')
    serializer_class = ChemSerializer
