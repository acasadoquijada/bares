import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica4.settings')

import django
django.setup()

from bares.models import Bar, Tapa


def populate():
    bar1 = add_bar('Bar1')

    add_tapa(bar=bar1,
        nombre="Tapa 1",
        votos=8)

    add_tapa(bar=bar1,
        nombre="Tapa 2",
        votos=9)

    add_tapa(bar=bar1,
        nombre="Tapa 3",
        votos=288)

    bar2 = add_bar('Bar2')

    add_tapa(bar=bar2,
        nombre="Tapa 4",
        votos=4)

    add_tapa(bar=bar2,
        nombre="Tapa 5",
        votos=1)

    add_tapa(bar=bar2,
        nombre="Tapa 6",
        votos=285)

    # Print out what we have added to the user.
    for c in Bar.objects.all():
        for p in Tapa.objects.filter(bar=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_tapa(bar, nombre, votos):
    p = Tapa.objects.get_or_create(bar=bar,nombre=nombre,votos=votos)[0]
    p.save()


def add_bar(name):
    c = Bar.objects.get_or_create(nombre=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Bares population script...")
    populate()
