from rest_framework.serializers import ModelSerializer
from users.models import Payments


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


# class PaymentDetailsSerializer(ModelSerializer):
#     class Meta:
#         model = Payments
#         fields = ('id', 'payment_date', 'course', 'lesson', 'payment_type', 'amount')
