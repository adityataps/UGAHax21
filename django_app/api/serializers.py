from rest_framework import serializers

from .models import Chart

class ChartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chart
        fields = ('b64_encoded', 'chart_type', 'chart_desc')
