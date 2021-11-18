from django.db.models import query
from requests import Response
from rest_framework import generics, permissions, viewsets
from .serializers import *
from .models import Logistic
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.shortcuts import render
# from .models.db import F

def oauth(request):
    return render(request, 'oauth.html')

class prosmotr(models.Model):
    model = Logistic
    template_name = ''
    context_object_name = 'logistic'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Logistic'
        context.update({
            'product':Logistic.objects.all(),
            'Views':Logistic.objects.filter(pk=Logistic.pk).update(views=F('views') + 1)
    })

class HitCountViewSet(viewsets.ModelViewSet):
    queryset = HitCount.objects.all()
    serializer_class = HitCountSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        HitCount.objects.filter(pk=instance.id).update(visits=F('visits') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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

class prosmotrDetailVies(generics.ListAPIView):
    serializer_class = LogisticAllSerializers
    queryset = Logistic.objects.all()
    permission_classes = (IsAuthenticated,)
