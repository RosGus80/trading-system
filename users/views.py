from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import SignUpSerializer, UserSerializer


# Create your views here.


class UserSignUpAPIView(generics.CreateAPIView):
    """Вью для регистрации новых пользователей"""
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Вью для просмотра профиля зарегистрированного пользователя. Выдаст ошибку, если будет введен неверный айди."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Вью для редактирования профиля зарегистрированного пользователя.
    Выдаст ошибку, если будет введен неверный айди."""
    serializer_class = SignUpSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


