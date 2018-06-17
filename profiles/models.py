from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from .utils import code_generator
User = settings.AUTH_USER_MODEL
# Create your models here.
from django.core.mail import send_mail


class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following=False

        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following




class Profile(models.Model):

    user            =   models.OneToOneField(User)
    followers       =   models.ManyToManyField(User, related_name='is_following',blank=True)
    activated       =   models.BooleanField(default=False)
    activation_key  =   models.CharField(max_length=120, blank=True, null = True)
    timestamp       =   models.DateTimeField(auto_now_add=True)
    updated         =   models.DateTimeField(auto_now=True)
    objects         =   ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):

        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            subject = 'Activation for MuyPicky.com'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activation Your Accoun:{self.activation_key}'
            recipient_list = [self.user.email]
            html_message =  f'Activation Your Accoun:{self.activation_key}'
        
            sent_mail = send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
            #print(send_mail)
            
           
        return sent_mail


def post_save_user_receiver(sender,instance,created, *args, **kwargs):
        if created:
            profile, is_created = Profile.objects.get_or_create(user=instance)
            default_user_profile = Profile.objects.get(user__id=1)
            default_user_profile.followers.add(instance)
            profile.followers.add(default_user_profile.user)

#signal post event
post_save.connect(post_save_user_receiver, sender=User)
    