from rest_framework import serializers
from .models import *

class LogisticAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Logistic
        fields = "__all__"
