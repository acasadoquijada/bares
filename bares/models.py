from django.db import models
from django.template.defaultfilters import slugify

class Bar(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    direccion = models.CharField(max_length=128)
    numero_visita = models.IntegerField(default=0)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        if self.id is None:
            self.slug = slugify(self.nombre)
        self.slug = slugify(self.nombre)
        super(Bar, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
        
    def votar(self):
        self.numero_visita +=1

class Tapa(models.Model):
    bar = models.ForeignKey(Bar)
    nombre = models.CharField(max_length=128)
    votos = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='imagenes_tapas', blank=True)
    def __str__(self):      
        return self.nombre
