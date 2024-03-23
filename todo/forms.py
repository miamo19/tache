from django import forms
from .models import Tache
 
 
class FomulaireTache(forms.ModelForm):
    class Meta:
        model = Tache
        fields = "__all__"