from django.db import models


class Chem(models.Model):

    CHEMICAL_CHARACTER = (
        ("ciało stałe", "1"),
        ("ciecz", "2"),
        ("gaz", "3"),
        ("prawdopodobnie ciało stałę", "4"),
        ("prawdopodobnie ciecz", "5"))
    PHYSICAL_CHOICES = (
        ("metal", "1"),
        ("niemetal", "2"),
        ("metal/półmetal", "3"),
        ("niemetal/półmetal", "4"),
        ("prawdopodobnie niemetal", "5"))
    shortcut = models.CharField(max_length=20, default="unknown")
    name = models.CharField(max_length=10, default="unknown")
    atomic_number = models.IntegerField(primary_key=True)
    atom_mass = models.CharField(max_length=20, default="unknown")
    physical_state = models.CharField(max_length=30, choices=PHYSICAL_CHOICES, default="unknown")
    chemical_character = models.CharField(max_length=30, choices=CHEMICAL_CHARACTER, default="unknown")
    density = models.CharField(max_length=20, default="unknown")
    melt_temp = models.CharField(max_length=10, default="unknown")
    boiling_temp = models.CharField(max_length=10, default="unknown")
    discover_year = models.CharField(max_length=30, default="unknown")
    discover = models.CharField(max_length=70, default="unknown")


