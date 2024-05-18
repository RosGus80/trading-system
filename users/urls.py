from django.urls import path

from users.views import UserSignUpAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = 'users'

urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('user_retrieve/<int:pk>', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('user_update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
    path('user_destroy/<int:pk>', UserDestroyAPIView.as_view(), name='user_destroy'),
]
