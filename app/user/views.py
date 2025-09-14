"""
View for the user API
"""

from rest_framework import generics

from user.seriealizers import UserSerializer



class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
