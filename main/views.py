from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from main.models import Factory, Entrepreneur, Product, Retailer
from main.paginators import BasePaginator
from main.serializers import ProductCreateSerializer, EntrepreneurCreateSerializer, FactoryCreateSerializer, \
    RetailerCreateSerializer, FactoryRetrieveSerializer, EntrepreneurRetrieveSerializer, ProductRetrieveSerializer, \
    RetailerUpdateSerializer, EntrepreneurUpdateSerializer, FactoryUpdateSerializer, RetailerRetrieveSerializer


# Create your views here.


class FactoryCreateAPIView(generics.CreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FactoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FactoryUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Factory.objects.filter(owner=self.request.user)


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FactoryRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Factory.objects.filter(owner=self.request.user)


class FactoryDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        Factory.objects.filter(owner=self.request.user)


class FactoryListAPIView(generics.ListAPIView):
    """Вью для вывода всех заводов из вашей базы данных. Может принять параметр 'country' для фильтрации по стране"""
    serializer_class = FactoryRetrieveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BasePaginator

    def get_queryset(self):
        try:
            if self.request.query_params.__len__() == 0:
                return Factory.objects.filter(owner=self.request.user).order_by('pk')
            else:
                return Factory.objects.filter(owner=self.request.user,
                                              country=self.request.query_params['country']).order_by('pk')
        except KeyError:
            raise ValidationError(detail="Принимается только параметр 'country'")


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EntrepreneurUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Entrepreneur.objects.filter(owner=self.request.user)


class EntrepreneurDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        Factory.objects.filter(owner=self.request.user)


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EntrepreneurRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Entrepreneur.objects.filter(owner=self.request.user)


class EntrepreneurListAPIView(generics.ListAPIView):
    """Вью для вывода всех ИП из вашей базы данных. Может принять параметр 'country' для фильтрации по стране"""
    serializer_class = EntrepreneurRetrieveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BasePaginator

    def get_queryset(self):
        try:
            if self.request.query_params.__len__() == 0:
                return Entrepreneur.objects.filter(owner=self.request.user).order_by('pk')
            else:
                return Entrepreneur.objects.filter(owner=self.request.user,
                                                   country=self.request.query_params['country']).order_by('pk')
        except KeyError:
            raise ValidationError(detail="Принимается только параметр 'country'")


class RetailerCreateAPIView(generics.CreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetailerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RetailerUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Retailer.objects.filter(owner=self.request.user)


class RetailerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RetailerRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Retailer.objects.filter(owner=self.request.user)


class RetailerDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        Retailer.objects.filter(owner=self.request.user)


class RetailerListAPIView(generics.ListAPIView):
    """Вью для вывода всех розничных сетей из вашей базы данных.
    Может принять параметр 'country' для фильтрации по стране"""
    serializer_class = RetailerRetrieveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BasePaginator

    def get_queryset(self):
        try:
            if self.request.query_params.__len__() == 0:
                return Retailer.objects.filter(owner=self.request.user).order_by('pk')
            else:
                return Retailer.objects.filter(owner=self.request.user,
                                               country=self.request.query_params['country']).order_by('pk')
        except KeyError:
            raise ValidationError(detail="Принимается только параметр 'country'")


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.object.filter(owner=self.request.user)


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductRetrieveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BasePaginator

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)
