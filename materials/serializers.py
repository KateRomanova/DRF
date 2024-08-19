from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    lessons_amount_in_course = serializers.SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons_amount_in_course(self, obj):
        if obj.lesson_set.all().count():
            return obj.lesson_set.all().count()
        else:
            return 0

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
