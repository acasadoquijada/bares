from django import forms
from bares.models import Bar, Tapa

class TapaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce el nombre de la tapa")
  
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapa
        fields = ('bar','nombre','imagen')
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
