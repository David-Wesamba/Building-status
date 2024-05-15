from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
from .utlity import rem, randText
import random
def homepage(request):
    text = randText()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Data.objects.all()
            pk = 1
            for item in obj:
                if item.id > pk:
                    pk = item.id
            print(pk)
            return redirect('view',pk)
    else:
        form = DataForm()
    context = {
        'form': form,
        'page':'home',
        "text": text
    }
    return render(request,'home.html',context)

def view(request, pk):
    obj = Data.objects.get(id=pk)
    help_c_array =['apply cement to fill up cracks',
                'paint the building',
                'sand the surface',
                'wall crack filler or crack filler for concrete'      
    ]
    help_r_array=[
        'Replace the Iron Sheets',
        'fill holes present on the iron sheets',
        'paint The sheets'
    ]
    help_a = ''
    help_r = ''
    help_c = ''
    explanation_facility = ['1','2','3','4','5','6','7']
    if obj.cracks:
        help_c = random.choice(help_c_array)
        explanation_facility[0] = 'cracks present' 
    else:
        explanation_facility[0] = 'cracks not visible'

    if obj.roofing:
        help_r = random.choice(help_r_array)
        explanation_facility[1] = 'it\'s roof leaks'
    else:
        explanation_facility[1] = 'it\'s does not leak'


    if obj.l_arrestors == 0:
        help_a = 'Install Arrestors'
        explanation_facility[2] = 'Ligthning Arrestors not installed'
    else:
        explanation_facility[2] = 'Ligthning Arrestors not installed'
    if obj.wall_thickness:
        explanation_facility[3] = 'it\'s walls are thick'
    else:
        explanation_facility[3] = 'it\'s walls are thin'
    if obj.anti_eathquake:
        explanation_facility[4] = 'anti earthquake designed'
    else:
        explanation_facility[4] = 'No anti earthquake designed'
    if obj.seismic_zone:
        explanation_facility[5] = 'it is located in seismic zone'
    else:
        explanation_facility[5] = 'it is located in safe zones'
    if obj.soil_type == 0:
        explanation_facility[6] = 'soil type is clay this provides weak support'
    elif obj.soil_type == 4:
        explanation_facility[6] = 'soil type is Rocky this provide strong support'
    elif obj.soil_type == 3:
        explanation_facility[6] = 'soil type is Loam this provide moderate support'
    elif obj.soil_type == 1:
        explanation_facility[6] = 'soil type is Silt this provide strong support'
    elif obj.soil_type == 2:
        explanation_facility[6] = 'soil type is Sandy this provide strong support'


    state = rem(obj.predictions)
    
    context={"object":obj,
            "state": state,
            'help_c':help_c,
            'help_r':help_r,
            'help_a':help_a,
            'exp_array':explanation_facility
         }
    return render(request,'viewtest.html', context)

def status(request):
    obj = Data.objects.all()
    text = ''

 
    context = {
        'objects': obj,
        'page':'status',
        'text': text,
        
    }
    
    return render(request,'pred.html',context)

def about(request):
    context ={'page':'about' }
    return render(request,'about.html', context)
