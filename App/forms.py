from django import forms
from .models import TipoVehiculo, Vehiculo, Marca

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
    
    
    fechavencimiento = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label='fecha de vencimiento')
    observaciones = forms.CharField(widget= forms.Textarea(attrs={'row': 4, 'cols': 50}))
    
    
    #Marca
    marcaId = forms.ModelChoiceField(queryset= Marca.objects.all(), label='Marca')
    marcaId.widget.attrs['class'] = 'form-select'
    
    #Tipo Vehiculo
    tipoVehiculoId = forms.ModelChoiceField(queryset= TipoVehiculo.objects.all(), label='Tipo Vehiculo')
    tipoVehiculoId.widget.attrs['class'] = 'form-select'
    
    def clean_patente(self):
        patente = self.cleaned_data.get('patente')
        if len(patente) != 6:
            raise forms.ValidationError("La patente debe tener 6 caracteres")
        return patente
    
    def clean_chasis(self):
        chasis = self.cleaned_data.get('chasis')
        if len(chasis) != 17:
            raise forms.ValidationError('El número del chasis debe tener 17 caracteres')
        return chasis
    
    def clean_motor(self):
        motor = self.cleaned_data.get('motor')
        if len(motor) != 17:
            raise forms.ValidationError('El numero del motor deve tener 17 caracteres')
        return motor
    
    def clean_observaciones(self):
        observaciones = self.cleaned_data('observaciones')
        palabras = observaciones.split()
        
        if len(palabras) < 5:
            raise forms.ValidationError('Las obsenvaciones deben contener al menos 5 palabras')
        return observaciones
    

   