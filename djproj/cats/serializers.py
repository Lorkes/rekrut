from rest_framework import serializers

from .models import Hunting


class HuntingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunting
        fields = ['cat_id', 'hunting_duration', 'hunting_prey']
