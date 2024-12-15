from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        checkins = data.get("checkin")
        checkouts = data.get("checkout")

        if checkins and checkouts and checkins > checkouts :
            raise serializers.ValidationError("Checkin date cannot be greater than Checkout date")
        return data
