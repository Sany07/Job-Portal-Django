from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from account.models.profiles import EmployeeProfile, EmployerProfile

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'employee':
            EmployeeProfile.objects.create(user=instance)
        elif instance.role == 'employer':
            EmployerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 'employee':
        if hasattr(instance, 'employee_profile'):
            instance.employee_profile.save()
    elif instance.role == 'employer':
        if hasattr(instance, 'employer_profile'):
            instance.employer_profile.save()
