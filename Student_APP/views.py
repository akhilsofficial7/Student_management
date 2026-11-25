from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from Student_APP.serializers import RegisterSerializer, StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Student_APP.models import StudentDb


# Create your views here.


class RegistrationView(APIView):

    def post(self, request):
        serializer_instance = RegisterSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response(
                data={"Message": "Registration Successful..!"},
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentListCreateView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        students = StudentDb.objects.filter(user=request.user)
        serializer_instance = StudentSerializer(students, many=True)

        return Response(serializer_instance.data)


    def post(self, request):
        serializer_instance = StudentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)

            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]


    def get_object(self, request, id):
        return get_object_or_404(StudentDb, id=id, user=request.user)


    def get(self, request, id):
        student = self.get_object(request, id)
        serializer = StudentSerializer(student)

        return Response(serializer.data)


    def put(self, request, id):
        student = self.get_object(request, id)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        student = self.get_object(request, id)
        student.delete()

        return Response({"message": "Student deleted successfully"})



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request):
        request.user.auth_token.delete()

        return Response({
            "Message": "Logout success..!"
        })