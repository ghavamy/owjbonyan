from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='videoIndex'),
    path('create/', views.CreateVideo.as_view(), name='create_video'),
    path('<int:pk>/', views.DetailVideo.as_view(), name='video_detail'),
    path('<int:pk>/update', views.UpdateVideo.as_view(), name='update_video'),
    path('<int:pk>/delete', views.DeleteVideo.as_view(), name='delete_video'),
    path('category/<int:pk>/', views.VideoCategoryList.as_view(), name='category_list'),
    path('search/', views.SearchVideo.as_view(), name='search_video'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)