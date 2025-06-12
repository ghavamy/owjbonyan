from django.db.models.signals import post_save
from django.dispatch import receiver
import os



@receiver(post_save, sender="profiles.Profile")
def fix_image_permissions(sender, instance, **kwargs):
    image_path = os.path.join(instance.image.path)
    os.system(f"chmod 755 {image_path}")