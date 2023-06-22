from django import forms
from .models import Perfil

from django.forms import ModelForm
from django.contrib.admin.widgets import autocomplete_light

class ProfileForm(ModelForm):

    class Meta:
        model = Perfil
        fields = ['user', 'telefono', 'foto']
        autocomplete_fields = ['user', 'telefono', 'foto']
        labels = {'user': 'Nombre de usuario', 'foto': 'Foto de perfil', 'telefono': 'Teléfono'}
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = autocomplete_light.AutocompleteLightWidget(
            url='profile-autocomplete'
        )

    def save(self, commit=True):
        profile = super().save(commit=False)

        # Do some custom logic here

        if commit:
            profile.save()

        return profile

def save_profile(request):
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        profile = form.save()
        return redirect('profile')
    else:
        return render(request, 'profile.html', {'form': form})
