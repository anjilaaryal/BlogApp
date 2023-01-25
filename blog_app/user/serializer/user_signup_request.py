from rest_framework import serializers

class SignUpRequest(serializers.Serializer):
    password = serializers.CharField(max_length = 100)
    email = serializers.CharField(max_length = 100)
    first_name = serializers.CharField(max_length = 100)
    contact_number = serializers.CharField(max_length = 100)

    

    
