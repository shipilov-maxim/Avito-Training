from cryptography.fernet import Fernet
import base64
from django.conf import settings


def encrypt(pas):
    try:
        pas = str(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('UTF-8'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("UTF-8")
        return encrypt_pass
    except Exception:
        print('Errror')
        return None


def decrypt(pas):
    try:
        pas = base64.urlsafe_b64decode(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        decod_pass = cipher_pass.decrypt(pas).decode("UTF-8")
        return decod_pass
    except Exception:
        print('Errror')
        return None
