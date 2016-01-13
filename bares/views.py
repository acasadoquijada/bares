from django.shortcuts import render
from django.http import HttpResponse
from bares.models import Bar, Tapa
from bares.forms import TapaForm

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    lista_bares = Bar.objects.order_by('-nombre')[:5]
    context_dict = {'bares': lista_bares}

    # Render the response and send it back!
    return render(request, 'bares/index.html', context_dict)
    
def about(request):
    return render(request,'bares/about.html')
    
def bares(request, bar_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        bar = Bar.objects.get(slug=bar_name_slug)
        context_dict['nombre_bar'] = bar.nombre
        context_dict['dire_bar'] = bar.direccion
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        tapas = Tapa.objects.filter(bar=bar)

        # Adds our results list to the template context under name pages.
        context_dict['tapas'] = tapas
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['bar'] = bar
        
        # Aumentamos el voto
        bar.votar()
        
        bar.save()
        
    except Bar.DoesNotExist:
    # We get here if we didn't find the specified category.
    # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'bares/bares.html', context_dict)
    
    
def add_tapa(request):

    if request.method == 'POST':
        form = TapaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print (form.errors)
    else:
        form = TapaForm()

    context_dict = {'form':form}

    return render(request, 'bares/add_tapa.html', context_dict)
        
        
        
