'''
Yes, Django signals run in the same thread as the caller. Signals do not create new threads unless explicitly set up to do so.
'''
#Code Example
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")


print(f"Main thread: {threading.current_thread().name}")
user = User.objects.create(username="test_user")
