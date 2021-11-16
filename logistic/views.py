from django.db.models import query
from rest_framework import generics, permissions
from .serializers import *
from .models import Logistic
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.shortcuts import render

def oauth(request):
    return render(request, 'oauth.html')


class LogisticCreateView(generics.CreateAPIView):
    serializer_class = LogisticAllSerializers
    permission_classes = (IsAuthenticated, IsAdminUser)

class LogisticListView(generics.ListAPIView):
    serializer_class = LogisticAllSerializers
    queryset = Logistic.objects.all()
    permission_classes = (IsAuthenticated,)

class LogisticDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LogisticAllSerializers
    queryset = Logistic.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    # authentication_classes = (TokenAuthentication, SessionAuthentication)


