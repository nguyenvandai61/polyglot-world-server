from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from app.models.MyUser import MyUser
from rest_framework import permissions

from app.mserializers.UserSerialziers import UserLearnProgressSerializer
User = get_user_model()
# from app.models.User import User


class MeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        first = request.user.first_name
        last = request.user.last_name
        
        return Response({
            'id': user_id,
            'username': username,
            'email': email,
            'first_name': first,
            'last_name': last,
        })
        
class DataLogin(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        name = request.user.first_name + ' ' + request.user.last_name
        avatar = request.user.avatar
        
        return Response({
            'id': user_id,
            'username': username,
            'email': email,
            'name': name,
            'avatar': avatar,
        })

class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')
        first = name.split(' ')[0]
        last = '' if len(name.split(' ')) == 1 else name.split(' ')[1]
        gender = request.data.get('gender')
        country = request.data.get('country')
        languages = request.data.get('languages')

        is_admin = False
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first,
                last_name=last,
                country=country,
                languages=languages,
                is_admin=is_admin,
                gender=gender
            )
        except Exception as e:
            return Response({
                'status': 'error',
                'error_code': e.args[0],
            }, status=400)
        
        return Response(
            {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
            }
        )


class MyLearnProgressAPI(APIView):
    serializer_class = UserLearnProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user_id = request.user.id
        user = MyUser.objects.get(id=user_id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)