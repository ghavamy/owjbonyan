from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import UpdateView
from django.urls import reverse
from .models import Profile
from videos.models import Video

# Create your views here.
class ProfileView(View):

    def get(self, request, pk, *args, **kwargs):
            
        profile = get_object_or_404(Profile, pk=pk)

        videos = Video.objects.all().filter(uploader=pk).order_by('-date_posted')

        context = {
            'profile': profile,
            'videos': videos
        }

        return render(request, 'profiles/profile.html', context)
    
class UpdateProfile(UpdateView):
    model = Profile
    fields = ['name', 'location', 'image']
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        if 'image' in self.request.FILES:  # Explicitly check if an image was uploaded
            form.instance.image = self.request.FILES['image']
        elif not form.instance.image or form.instance.image == '':  # Assign default only if no image exists
            form.instance.image = 'uploads/profile_pics/default.jpg'
        return super().form_valid(form)

    
    def get_success_url(self):
        return reverse ('profiles:profile', kwargs={'pk': self.object.pk})