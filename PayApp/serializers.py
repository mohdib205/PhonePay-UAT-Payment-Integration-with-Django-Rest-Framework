from rest_framework import serializers
from .models import * 


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentResponse
        fields='__all__'
        # exclude="payment_instrument"
