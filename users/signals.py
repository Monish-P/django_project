from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile

@receiver(post_save, sender=User)
#reciver is a decorator,here the signal(here post_save) will be triggered 
#whenever an instance of the sender (here User) gets saved.And what function to
#execute when the signal gets triggered.
def create_profile(sender,instance,created,**kwargs):
    if created:
        created_profile=profile(user=instance)
        created_profile.save()
    
    

