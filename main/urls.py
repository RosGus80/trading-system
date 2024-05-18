from django.urls import path

from main.views import *

app_name = 'main'


urlpatterns = [
    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory_create'),
    path('factory/<int:pk>/update', FactoryUpdateAPIView.as_view(), name='factory_update'),
    path('factory/<int:pk>', FactoryRetrieveAPIView.as_view(), name='factory_retrieve'),
    path('factory/<int:pk>/delete', FactoryDestroyAPIView.as_view(), name='factory_delete'),
    path('factory/list', FactoryListAPIView.as_view(), name='factory_list'),

    path('retailer/create/', RetailerCreateAPIView.as_view(), name='retailer_create'),
    path('retailer/<int:pk>/update', RetailerUpdateAPIView.as_view(), name='factory_update'),
    path('retailer/<int:pk>', RetailerRetrieveAPIView.as_view(), name='retailer_retrieve'),
    path('retailer/<int:pk>/delete', RetailerDestroyAPIView.as_view(), name='retailer_delete'),

    path('entrepreneur/create/', EntrepreneurCreateAPIView.as_view(), name='entrepreneur_create'),
    path('entrepreneur/<int:pk>/update', EntrepreneurUpdateAPIView.as_view(), name='factory_update'),
    path('entrepreneur/<int:pk>', EntrepreneurRetrieveAPIView.as_view(), name='entrepreneur_retrieve'),
    path('entrepreneur/<int:pk>/delete', EntrepreneurDestroyAPIView.as_view(), name='entrepreneur_delete'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/<int:pk>', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/<int:pk>/delete', ProductDestroyAPIView.as_view(), name='product_delete'),
]
