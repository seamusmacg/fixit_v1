from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=18, null=False, blank=False)
    default_postcode = models.CharField(max_length=15, null=True, blank=True)
    default_town = models.CharField(max_length=50, null=False, blank=False)
    default_address = models.CharField(max_length=100, null=False, blank=False)
    default_country = CountryField(
        blank_label='Country *', null=False, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_update(sender, instance, created, **kwargs):
    """Save the profile to user"""
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
    instance.profile.save()
