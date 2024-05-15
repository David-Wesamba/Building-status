from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib


OCCUPANCY = (
    (0, 'Commercial'),
    (1, 'Residential'),
    (2, 'Industrial'),
)
ZONE = (
    (0, 'No'),
    (1, 'Yes'),
)
CRACKS= (
    (0, 'No'),
    (1, 'Yes'),
)
LA= (
    (0, 'No'),
    (1, 'Yes'),
)
EQ= (
    (0, 'No'),
    (1, 'Yes'),
)
ROOFING= (
    (0, 'No leaks'),
    (1, 'Leaks'),
)
WALL= (
    (0, 'Thin'),
    (1, 'Thick'),
)
SOIL= (
    (0, 'Clay'),
    (1, 'Silt'),
    (2, 'Sandy'),
    (3, 'Loam'),
    (4, 'Rocky'),
)


class Data(models.Model):
    name = models.CharField(max_length=10,null=True)
    occupancy = models.PositiveIntegerField(choices=OCCUPANCY, null=True)
    floors = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)], null=True)
    roofing = models.PositiveIntegerField(choices=ROOFING, null=True)
    seismic_zone = models.PositiveIntegerField(choices=ZONE, null=True)
    cracks = models.PositiveIntegerField(choices=CRACKS, null=True)
    l_arrestors = models.PositiveIntegerField(choices=LA, null=True)
    anti_eathquake = models.PositiveIntegerField(choices=EQ, null=True)
    soil_type = models.PositiveIntegerField(choices=SOIL, null=True)
    wall_thickness = models.PositiveIntegerField(choices=WALL, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

# new_building = model.predict([[a,b,x,c,w,z,y,d,e]])
# new_building

    def save(self, *args, **kwargs):
        model = joblib.load('model/meta.joblib')
        self.predictions = model.predict([[self.seismic_zone,self.occupancy,self.floors,self.roofing,self.cracks,self.l_arrestors,self.anti_eathquake,self.soil_type,self.wall_thickness]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
