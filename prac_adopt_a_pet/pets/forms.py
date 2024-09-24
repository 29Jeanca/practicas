from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['age', 'weight', 'species', 'color']

    # Sobrescribimos el campo species para que sea un dropdown cargado con valores únicos de la base de datos
    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        
        # Obtener todas las especies únicas de la base de datos
        especies = Animal.objects.values_list('species', flat=True).distinct()
        
        # Convertir las especies en una lista de tuplas (opciones del dropdown)
        opciones_especies = [(especie, especie.capitalize()) for especie in especies]
        
        # Definir el campo species como ChoiceField con las opciones dinámicas
        self.fields['species'] = forms.ChoiceField(choices=opciones_especies, required=True, label="Seleccione la especie")

    # Validaciones adicionales
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise forms.ValidationError("La edad no puede ser negativa.")
        return age

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight <= 0:
            raise forms.ValidationError("El peso debe ser mayor que 0.")
        return weight
