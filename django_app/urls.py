from django.urls import path
from .views import UserAPIView, SendEmailView, EmailMessageListView

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),
    path('send-email/', SendEmailView.as_view()),
    path('email-messages/', EmailMessageListView.as_view()),
]
