from rest_framework import serializers
from .models import Chem


class ChemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chem
        fields = ('shortcut', 'name', 'atomic_number', 'atom_mass', 'physical_state',
                  'chemical_character', 'density', 'melt_temp', 'boiling_temp', 'discover_year', 'discover')
