from rest_framework import serializers

from app.models.MyUser import MyUser


class ProfileSerializer(serializers.ModelSerializer):
    streak_count = serializers.SerializerMethodField()
    total_exp = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff',
                  'gender',
                  'is_active', 'last_login', 'date_joined', 'groups', 'avatar', 'country',
                  'streak_count', 'total_exp')

    def get_streak_count(self, user):
        return user.learn_progress.streak_count

    def get_total_exp(self, user):
        return user.learn_progress.total_exp
