from rest_framework import serializers

from tpapp.models import AppData


class TpAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppData
        fields = '__all__'
