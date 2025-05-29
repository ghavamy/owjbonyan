from django.urls import path
from .views import ProfileView, UpdateProfile
from django.conf import settings
from django.conf.urls.static import static

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update', UpdateProfile.as_view(), name='update_profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)