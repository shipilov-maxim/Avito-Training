from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app.models import Secret


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = '__all__'


# class CourseDetailSerializer(serializers.ModelSerializer):
#     count_lesson_in_course = SerializerMethodField()
#     lessons = LessonSerializer(many=True)
#     is_subscribed = serializers.SerializerMethodField()
#
#     def get_count_lesson_in_course(self, instance):
#         return instance.lessons.count()
#
#     def get_is_subscribed(self, instance):
#         return instance.subscriptions.exists()
#
#     class Meta:
#         model = Course
#         fields = '__all__'
