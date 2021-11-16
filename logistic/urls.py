from django.urls import path, include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('v1/logic/create', LogisticCreateView.as_view()),
    path('v1/logistic/list', LogisticListView.as_view()),
    path('v1/logistic/detail/<int:pk>', LogisticDetailView.as_view()),
]
