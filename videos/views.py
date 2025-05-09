from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

from .models import Video

# Create your views here.
def videoIndex(request):
    return render(request , 'videos/videoIndex.html')

class CreateVideo(CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse('video_detail', kwargs={'pk': self.object.pk})

class DetailVideo(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'

class UpdateVideo(UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse('video_detail', kwargs={'pk': self.object.pk})
    
class DeleteVideo(DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse('videoIndex')