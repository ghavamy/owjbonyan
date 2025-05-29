from django import forms
from .models import Profile

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name')
    location = forms.CharField(max_length=80, label='Location')
    image = forms.ImageField(label='Profile Image', required=False)

    class Meta:
        model = Profile
        fields = ['name', 'location', 'image']
    
    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user = user
        profile.name = self.cleaned_data['name']
        profile.location = self.cleaned_data['location']
        profile.image = self.cleaned_data.get('image', 'uploads/profile_pics/default.jpg')
        profile.save()