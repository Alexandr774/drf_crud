import factory.django

from autentication.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test_user"
    password = 0000