import random
def rem(pred):
    state = ''
    for char in pred:
        if char == "[":
            continue
        elif char == "]":
            continue
        elif char == "\'":
            continue
        else:
            state  += char
    return state

def randText():
    my_array = ['Hello there ' ,'Good to see you', 'Hi ']
    greetings = random.choice(my_array)
    return greetings

def help(object):   
    help_c = ['apply cement to fill up cracks',
                'paint the building',
                'sand the surface',
                'wall crack filler or crack filler for concrete'      
    ]
    help_r=[
        'Replace the Iron Sheets',
        'fill holes present on the iron sheets',
        'paint The sheets'
    ]
    help_arrestor=[
        'Install Arrestors'
    ]

