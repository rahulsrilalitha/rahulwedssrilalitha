#from django import forms


#class EngagementImageUploadForm(forms.Form):
#    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected ': True}))

from django import forms
from .models import Engagement


class EngagementForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Engagement
        fields = ('title', 'image')