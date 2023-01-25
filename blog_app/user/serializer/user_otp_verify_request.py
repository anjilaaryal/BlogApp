from rest_framework import serializers

class OtpVerifyRequest(serializers.Serializer):
    otp = serializers.IntegerField()  #Find a way u restrict number entered by user
    email = serializers.CharField(max_length = 100)