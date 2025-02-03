
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import UserProfile

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
         
            try:
                user_profile = UserProfile.objects.get(user=user)
                role = user_profile.role
            except UserProfile.DoesNotExist:
                role = 'user'  

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'access': access_token,
                'refresh': str(refresh),
                'role': role,
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=400)