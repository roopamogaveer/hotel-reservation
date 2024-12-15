from rest_framework.views import APIView
from .serializers import ReservationSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation


# Create your views here.
class ReservationView(APIView):
    def post(self, request, format=None):
        try:
            serializer = ReservationSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)

            if serializer.errors.get("user"):
                message = "User doesn't Exist!"
            elif "Checkin" in serializer.errors.get("non_field_errors")[0]:
                message = "Checkin date cannot be greater than Checkout date"
            else:
                message = serializer.errors
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AllReservationView(APIView):
    def get(self, request, format=None):
        try:
            result = Reservation.objects.all()
            responseData = ReservationSerializer(result, many=True)
            return Response(responseData.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReservationbyUserIdView(APIView):
    def get(self, request, user):
        try:
            if Reservation.objects.filter(user=user).exists():
                reservation = Reservation.objects.filter(user=user)
                if reservation is not None:
                    result = ReservationSerializer(reservation, many=True)
                    return Response(data=result.data, status=status.HTTP_200_OK)
            else:
                message = "User doesn't Exist!"
                return Response(message, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReservationbyUserIdAndBookingIdView(APIView):
    def get(self, request, user, id):
        try:
            if Reservation.objects.filter(user = user).exists():
                reservation = Reservation.objects.filter(user=user, id=id).first()
                if reservation is not None:
                    result = ReservationSerializer(reservation)
                    return Response(data=result.data, status=status.HTTP_200_OK)
                else:
                    message = "Reservation doesn't Exist!"
                    return Response(message, status=status.HTTP_404_NOT_FOUND)
            else:
                message = "User doesn't Exist!"
                return Response(message, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

