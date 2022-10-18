
from .models import User, UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('created the user profile')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('profile is updated') 

        except:
            UserProfile.objects.create(user=instance)
            print('Profile was not exist, but created new one')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')
