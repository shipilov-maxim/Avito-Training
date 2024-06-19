from django.contrib import admin
from django.urls import path

from app.views import home, SecretCreateAPIView, SecretRetrieveAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('secret/', SecretCreateAPIView.as_view()),
    path('secret/<password>', SecretRetrieveAPIView.as_view()),
]
