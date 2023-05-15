from rest_framework import serializers


class TemporalModelSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'created_at',
            'updated_at',
        )
