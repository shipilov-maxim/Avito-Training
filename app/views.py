from django.http.response import JsonResponse
from rest_framework import generics

from app.models import Secret
from app.serializers import SecretSerializer
from app.utils import encrypt, decrypt


def home(request):
    return JsonResponse({"hello": "world"})


class SecretCreateAPIView(generics.CreateAPIView):
    serializer_class = SecretSerializer

    def perform_create(self, serializer):
        self.serializer_class = serializer.save()
        print(self.serializer_class.password)
        if self.serializer_class.password is None:
            self.serializer_class.password = encrypt(self.serializer_class.message)
        self.serializer_class.message = encrypt(self.serializer_class.message)
        self.serializer_class.save()


class SecretRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()

    def get_object(self, *args, **kwargs):
        try:
            secret = self.queryset.get(password=(self.kwargs.get('password')))
            secret.message = decrypt(secret.message)
            self.queryset.get(password=(self.kwargs.get('password'))).delete()
        except Secret.DoesNotExist:
            return print('Secret DoesNotExist')
        return secret
