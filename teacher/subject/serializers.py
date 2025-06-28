from rest_framework import serializers
from .models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def validate_title(self, title):
        list_of_titles = set(["Python", "Java", "C++", "C#"])
        if title in list_of_titles:
            return title
        raise serializers.ValidationError(f"Kurs Tabylbady: {list_of_titles}")