from django.shortcuts import render
from .models import subject, teacher
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import SubjectSerializer, SubjectCreatorSerializer, TeacherSerializer, TeacherCreatorSerializer


@api_view(["GET", "POST"])
def subject(request):
    method = request.method

    if method == "GET":
        subjects = subject.objects.all()
        stud_serializer = SubjectSerializer(subjects, many=True)

        return Response(stud_serializer.data, status=status.HTTP_200_OK)
    elif method == "POST":
        crete_serializer = SubjectCreatorSerializer(data=request.data)

        if crete_serializer.is_valid():
            subject = crete_serializer.save()

            serializer = SubjectCreatorSerializer(subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(
        {"message": f"Hello this is {method} method type"}, status=status.HTTP_200_OK
    )


@api_view(["GET", "POST"])
def teacher(request):
    method = request.method

    if method == "GET":
        teachere = teacher.objects.all()
        cour_serializer = TeacherSerializer(teachere, many=True)

        return Response(cour_serializer.data, status=status.HTTP_200_OK)
    elif method == "POST":
        crete_serializer = TeacherCreatorSerializer(data=request.data)

        if crete_serializer.is_valid():
            teachere = crete_serializer.save()

            serializer = TeacherCreatorSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": f"kurs tabylbady"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"message": f"Hello this is {method} method type"}, status=status.HTTP_200_OK
    )