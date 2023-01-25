
from django.urls import path
from user.views import UserSignUpView, UserLoginView, VerifyOtpView, FetchUserView

urlpatterns = [
    path('', FetchUserView.as_view()),
    path('signup', UserSignUpView.as_view()),
    path('login', UserLoginView.as_view()),
    path('verify/otp', VerifyOtpView.as_view()),
]