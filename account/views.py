from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (RegisterSerializer, ActivationSerializer, LoginSerializer)



class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = f'Поздравляем! Вы успешно зарегистрированы на нашем сайте. ' \
                      f'На указанный email адрес отправлено письмо с активационным кодом.'
            return Response(message, status=201)


class ActivationView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Ваш аккаунт активирован!')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы вышли из аккаунта')

