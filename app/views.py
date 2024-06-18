from django.http.response import JsonResponse
from rest_framework import generics
from faker import Faker

from app.models import Secret
from app.serializers import SecretSerializer


# from .tasks import create_random_posts


def post_generator(request):
    # create_random_posts.delay()
    fake = Faker()
    Secret.objects.create(message=fake.text())
    return JsonResponse({"success": True})


class SecretCreateAPIView(generics.CreateAPIView):
    serializer_class = SecretSerializer
