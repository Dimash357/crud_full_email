from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import User, EmailMessage
from .serializers import UserSerializer, EmailMessageSerializer
from django_app.tasks.send_email import send_email_task


class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class SendEmailView(APIView):
    def post(self, request):
        user_ids = request.data.get('users', [])
        message = request.data.get('message', '')
        subject = "Notification"

        if not user_ids or not message:
            return Response(
                {"error": "Both 'users' and 'message' fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users = User.objects.filter(id__in=user_ids)
        recipient_list = [user.email for user in users]

        if not recipient_list:
            return Response(
                {"error": "No valid users found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        send_email_task.delay(subject, message, recipient_list)
        return Response({"message": "Emails are being sent"})


class EmailMessageListView(ListAPIView):
    queryset = EmailMessage.objects.all().order_by('-created_at')
    serializer_class = EmailMessageSerializer
