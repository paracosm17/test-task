from django.db import IntegrityError
from users.models import CustomUser

try:
    superuser = CustomUser.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin')
    superuser.save()
except IntegrityError:
    print(f"Super User with this username is already exist!")
except Exception as e:
    print(e)
