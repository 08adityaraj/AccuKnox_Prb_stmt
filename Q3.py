'''
Yes, Django signals, particularly those connected to database-related events like
post_save and pre_save, run within the same database transaction as the caller by
default. This means that if the signal handler modifies the database and the
original transaction is rolled back, the changes made by the signal handler are also rolled back.
'''
#Code Example

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    print("Signal handler started.")
    # Modify the instance
    instance.username = "modified_user"
    instance.save()
    print("Signal handler finished.")

try:
    with transaction.atomic():
        user = User.objects.create(username="test_user")
        raise Exception("Simulate error after user creation")
except Exception as e:
    print("Transaction rolled back.")


user = User.objects.filter(username="modified_user").exists()
print("Was the signal handler's change saved?", user)
