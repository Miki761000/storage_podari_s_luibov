from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='users',
        blank=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.profile.save()