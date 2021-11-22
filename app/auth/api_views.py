from rest_framework.response import Response
from rest_framework.views import APIView


class MeAPIView(APIView):
    def get(self, request):
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        first = request.user.first_name
        last = request.user.last_name
        
        return Response({
            'user_id': user_id,
            'username': username,
            'email': email,
            'first_name': first,
            'last_name': last,
        })