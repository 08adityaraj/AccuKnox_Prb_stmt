'''
By default, Django signals are executed synchronously. When a signal is sent, the connected signal handler executes immediately before the rest of the code continues, meaning the signal blocks the calling code until it completes.
'''
#Code Example
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulating a delay
    print("Signal handler finished.")

# Simulating a User save to trigger the signal
user = User.objects.create(username="test_user")
print("User created.")


