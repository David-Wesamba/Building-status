from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'occupancy', 'floors', 'roofing','seismic_zone','cracks','l_arrestors', 'anti_eathquake'
                    ,'soil_type','wall_thickness']
