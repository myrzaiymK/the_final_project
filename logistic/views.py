from django.db.models import query
from django.views.generic.base import View
from requests import Response
from rest_framework import generics, permissions, viewsets
from .serializers import *
from .models import Logistic
from .permissions import *
from django.forms import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.shortcuts import render
# from .models.db import F





class prosmotr(View):
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
    authentication_classes = (TokenAuthentication, SessionAuthentication)

class prosmotrDetailVies(generics.ListAPIView):
    serializer_class = LogisticAllSerializers
    queryset = Logistic.objects.all()
    permission_classes = (IsAuthenticated,)


# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         form = LoginForm(request.POST or None)
#         categories = Category.objects.all()
#         context = {'form': form, 'categories': categories}
#         return render(request, 'seo/login.html', context)
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#         return render(request, 'seo/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request,
                'seo/register.html',
                {'new_user': new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'seo/register.html',
        {'user_form': user_form}
    )

