from rest_framework import serializers
from .models import BLog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BLog
        fields = '__all__'