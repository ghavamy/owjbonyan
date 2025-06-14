from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView
from django.views import View
from .models import Video, Comment, Category
from .forms import CommentForm

# Create your views here.
class Index(ListView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()

        context = {
            'categories': categories,
        }

        return render(request, 'videos/videoIndex.html', context)

class CreateVideo(LoginRequiredMixin , CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail','category']
    template_name = 'videos/create_video.html'

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('video_detail', kwargs={'pk': self.object.pk})

class DetailVideo(View):
    def get(self,request, pk, *args, **kwargs):
        video = Video.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-created_on')
        categories = Video.objects.filter(category = video.category)[:15]

        context = {
            'object': video,
            'comments': comments,
            'categories': categories,
            'form': form
        }

        return render(request, 'videos/video_detail.html', context)

    def post(self,request, pk, *args, **kwargs):
        video = Video.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                user= self.request.user,
                comment=form.cleaned_data['comment'],
                video=video
            )
            comment.save()

        comments = Comment.objects.filter(video=video).order_by('-created_on')
        categories = Video.objects.filter(category = video.category)[:15]

        context = {
            'object': video,
            'comments': comments,
            'categories': categories,
            'form': form
        }

        return render(request, 'videos/video_detail.html', context)

class UpdateVideo(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse('video_detail', kwargs={'pk': self.object.pk})
    
    def test_func (self):
        video = self.get_object()
        return self.request.user == video.uploader

    
class DeleteVideo(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse('videoIndex')
    
    def test_func (self):
        video = self.get_object()
        return self.request.user == video.uploader
    
class VideoCategoryList(View):
    def get(self,request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        videos = Video.objects.filter(category=category).order_by('-date_posted')
        context = {
            'category': category,
            'videos': videos
        }

        return render(request, 'videos/video_category.html', context)
    
class SearchVideo(View):
    def get(self,request, *args, **kwargs):
        query = self.request.GET.get("q")

        query_list = Video.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(uploader__username__icontains=query) 
        )

        context = {
            'query_list': query_list,
        }

        return render(request, 'videos/search_video.html', context)