from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import OtpVerifyRequest
from user.models import User, OtpUser



class VerifyOtpView(APIView):
    """Verify otp for user"""

    def post(self, request):
        req_data = request.data
        request_data = OtpVerifyRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        email = req_data["email"]
        otp = req_data["otp"]
        user_qs = User.objects.filter(email = email)
        if user_qs.exists():
            user_instance = user_qs[0]
            otp_qs = OtpUser.objects.filter(user = user_instance, otp_value = otp)
            if otp_qs.exists():
                User.objects.filter(email = email).update(otp_verified= True)
                return Response({"msg" : "OTP verified successfully"}, status = 200)
            else:
                return Response({"msg" : "OTP does not match"}, status = 400)
        else:
            return Response({"msg" : "Please enter a valid email"}, status = 400)