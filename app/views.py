from django.http.response import JsonResponse
from rest_framework import generics

from app.models import Secret
from app.serializers import SecretSerializer
from app.utils import encrypt, decrypt


def home(request):
    return JsonResponse({"go_to": "http://127.0.0.1:8000/secret/"})


class SecretCreateAPIView(generics.CreateAPIView):
    serializer_class = SecretSerializer
    """    APIView создания секрета, кодирует сообщение для
    конфеденциальности в базе данных. Если нет пароля,
    использует вместо него шифрованный секрет.    """
    def perform_create(self, serializer):
        self.serializer_class = serializer.save()
        if self.serializer_class.password is None:
            self.serializer_class.password = encrypt(self.serializer_class.message)
        else:
            self.serializer_class.password = encrypt(self.serializer_class.password)
        self.serializer_class.message = encrypt(self.serializer_class.message)
        self.serializer_class.save()


class SecretRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()

    """
    APIView получения секрета по паролю. Перед получением
    происходит расшифровка секрета.
    После получения удаляет из БД.
    """

    def get_object(self, *args, **kwargs):
        try:
            secret = self.queryset.get(password=(self.kwargs.get('password')))
            secret.message = decrypt(secret.message)
            self.queryset.get(password=(self.kwargs.get('password'))).delete()
        except Secret.DoesNotExist:
            return None
        return secret
