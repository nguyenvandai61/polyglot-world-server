from rest_framework import serializers

from app.models.MyUser import MyUser


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff',
                  'is_active', 'last_login', 'date_joined', 'groups', 'avatar', 'country')
