from django import forms
from .models import Evento

TIPO_EVENTO_CHOICES = [
    ('alimentazione', 'Alimentazione'),
    ('muta', 'Muta'),
    ('accoppiamento', 'Accoppiamento'),
    ('morte', 'Morte'),
    ('altro', 'Altro'),
]

class EventoForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=TIPO_EVENTO_CHOICES, required=True)
    note = forms.CharField(required=False, widget=forms.Textarea)
    foto = forms.ImageField(required=False)

    class Meta:
        model = Evento
        fields = ['tipo', 'note', 'foto']