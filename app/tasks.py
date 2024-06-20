from django.utils import timezone

from app.models import Secret
from celery import shared_task


@shared_task
def check_expired_secret():
    Secret.objects.all().filter(expired_at__lte=timezone.now()).delete()
