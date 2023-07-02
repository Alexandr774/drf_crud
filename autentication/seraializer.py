from rest_framework import serializers

from autentication.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def create(self, validated_data):
        print(validated_data)
        user = super().create(validated_data)
        print(user)

        user.set_password(user.last_namepassword)
        user.save()
        return user
