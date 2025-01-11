from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import UserModel, ChechingModel, USER_ROLES, USER_STATUS, CHECKING_STATUS

class UserModelSerializer(serializers.Serializer):
    finger_id = serializers.CharField(
        max_length=3,
        validators=[
            RegexValidator(r'^\d+$', message="FINGER ID must be numeric.")
        ]
    )
    full_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    role = serializers.ChoiceField(choices=USER_ROLES, required=False)
    status = serializers.ChoiceField(choices=USER_STATUS, required=False)

    def create(self, validated_data):
        # Yangi foydalanuvchi yaratish
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Foydalanuvchini yangilash
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ChechingModelSerializer(serializers.Serializer):
    user = UserModelSerializer()  # UserModelSerializer ichida
    checking_status = serializers.ChoiceField(choices=CHECKING_STATUS)
    time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # user ma'lumotlarini ajratib oling
        user = UserModel.objects.create(**user_data)  # Yangi user yarating
        return ChechingModel.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)  # user ma'lumotlarini ajratib oling
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)  # Foydalanuvchi ma'lumotlarini yangilang
            instance.user.save()  # Foydalanuvchi ma'lumotlarini saqlang

        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # ChekingModel ma'lumotlarini yangilang
        instance.save()  # Saqlang
        return instance
    



class ChechingModelCreateSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    checking_status = serializers.ChoiceField(choices=CHECKING_STATUS)
    time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user = validated_data.pop('user')  
        return ChechingModel.objects.create(user=user, **validated_data)