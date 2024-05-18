"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="API для ведения учета за торговой сетью.",
        default_version='v1',
        description="API для ведения учета за торговой сетью. Чтобы начать вести учет, "
                    "нужно зарегистрировать пользователя по адресу /users/signup и начать создавать элементы "
                    "торговой сети, зарегистрировавшись от имени этого пользователя. Авторизация происходит с помощью "
                    "bearer token'ов, срок жизни которых составляет один день. Чтобы ваши сотрудники могли вести учет "
                    "торговой сети от имени соответствующего пользователя, предоставляйте им актуальные логин и пароль."
                    "В документации ниже представлены инструкции для использования каждого эндпойнта.",
        terms_of_service="",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls', namespace='main')),
    path('users/', include('users.urls', namespace='users')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
