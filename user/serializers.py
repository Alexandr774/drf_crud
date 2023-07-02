from rest_framework import serializers

from user.models import User, Location, Ad


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        # many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=True)
    # location = serializers.SlugRelatedField(
    #     required=False,
    #     queryset=Location.objects.all(),
    #     slug_field='name'
    # )

    class Meta:
        model = User
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='first_name'
    )
    # category = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='name'
    # )

    class Meta:
        model = Ad
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        # many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

