
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'date_registered', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'age', 'phone_number']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class MarkaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ['marka_name']


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ['id', 'marka_name']


class ModelSerializer(serializers.ModelSerializer):
    marka = MarkaSimpleSerializer()

    class Meta:
        model = Model
        fields = ['id', 'marka', 'model_name']


class ModelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name']


class CarPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = ['model', 'images']


class CarPhotosSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = ['images']


class CarListSerializer(serializers.ModelSerializer):
    model = ModelSimpleSerializer()
    photos = CarPhotosSimpleSerializer(read_only=True, many=True)
    year_of_release = serializers.DateField(format='%Y')
    price_som = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'model', 'photos', 'year_of_release', 'price_dollars', 'price_som']

    def price_som(self, obj):
        return obj.som_total()


class CartSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    car = CarListSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'car']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y-%H-%M')
    car = CarListSerializer()
    author = UserProfileSimpleSerializer()

    class Meta:
        model = Review
        fields = ['id', 'author', 'text', 'car', 'parent_review', 'created_date']


class CarDetailSerializer(serializers.ModelSerializer):
    marka = MarkaSimpleSerializer()
    model = ModelSimpleSerializer()
    photos = CarPhotosSimpleSerializer(read_only=True, many=True)
    year_of_release = serializers.DateField(format='%Y')
    price_som = serializers.SerializerMethodField( )
    owner = UserProfileSimpleSerializer()
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = ['id', 'marka', 'model', 'photos',  'year_of_release', 'price_dollars', 'price_som', 'mileage',
                  'the_body', 'colour', 'engine', 'box_ru', 'box_en', 'box_kg', 'drive_ru', 'drive_en', 'drive_kg', 'rudder_ru', 'rudder_en', 'rudder_kg',
                  'condition', 'customs', 'exchange', 'availability', 'region_city_of_ale',
                  'accounting', 'other', 'text', 'owner','reviews']

    def price_som(self, obj):
        return obj.price_som()
