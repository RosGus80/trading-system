from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from main.models import Factory, Product, Entrepreneur, Retailer


class FactoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        exclude = ('owner', 'created_at',)


class FactoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        exclude = ('owner', 'created_at', 'total_supplier_debt',)


class FactoryRetrieveSerializer(serializers.ModelSerializer):
    contacts = SerializerMethodField()
    products = SerializerMethodField()

    def get_products(self, obj):
        obj_products = Product.objects.filter(factory_owner=obj)
        output = []
        if obj_products is None:
            return None
        else:
            for product in obj_products:
                product_info = {'name': product.name, 'pk': product.pk, 'version': product.version}
                if product.factory_supplier is not None:
                    product_info['supplier'] = f'Factory {product.factory_supplier.name} no. ' \
                                               f'{product.factory_supplier.pk}'
                elif product.retailer_supplier is not None:
                    product_info['supplier'] = f'Retailer {product.retailer_supplier.name} no. ' \
                                               f'{product.retailer_supplier.pk}'
                elif product.entrepreneur_supplier is not None:
                    product_info['supplier'] = f'Entrepreneur {product.entrepreneur_supplier.name} no. ' \
                                               f'{product.entrepreneur_supplier.pk}'
                else:
                    product_info['supplier'] = ''

                output.append(product_info)

        return output

    def get_contacts(self, obj):
        return {'email': obj.email, 'country': obj.country, 'city': obj.city,
                'street': obj.country, 'house_number': obj.house_number}

    class Meta:
        model = Factory
        exclude = ('owner', 'email', 'country', 'city', 'street', 'house_number')


class EntrepreneurCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        exclude = ('owner', 'created_at',)


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        exclude = ('owner', 'created_at', 'total_supplier_debt',)


class EntrepreneurRetrieveSerializer(serializers.ModelSerializer):
    contacts = SerializerMethodField()
    products = SerializerMethodField()

    def get_products(self, obj):
        obj_products = Product.objects.filter(entrepreneur_owner=obj)
        output = []
        if obj_products is None:
            return None
        else:
            for product in obj_products:
                product_info = {'name': product.name, 'pk': product.pk, 'version': product.version}
                if product.factory_supplier is not None:
                    product_info['supplier'] = f'Factory {product.factory_supplier.name} no. ' \
                                               f'{product.factory_supplier.pk}'
                elif product.retailer_supplier is not None:
                    product_info['supplier'] = f'Retailer {product.retailer_supplier.name} no. ' \
                                               f'{product.retailer_supplier.pk}'
                elif product.entrepreneur_supplier is not None:
                    product_info['supplier'] = f'Entrepreneur {product.entrepreneur_supplier.name} no. ' \
                                               f'{product.entrepreneur_supplier.pk}'
                else:
                    product_info['supplier'] = ''

                output.append(product_info)

        return output

    def get_contacts(self, obj):
        return {'email': obj.email, 'country': obj.country, 'city': obj.city,
                'street': obj.country, 'house_number': obj.house_number}

    class Meta:
        model = Entrepreneur
        exclude = ('owner', 'email', 'country', 'city', 'street', 'house_number')


class RetailerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        exclude = ('owner', 'created_at',)


class RetailerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        exclude = ('owner', 'created_at', 'total_supplier_debt',)


class RetailerRetrieveSerializer(serializers.ModelSerializer):
    contacts = SerializerMethodField()
    products = SerializerMethodField()

    def get_products(self, obj):
        obj_products = Product.objects.filter(retailer_owner=obj)
        output = []
        if obj_products is None:
            return None
        else:
            for product in obj_products:
                product_info = {'name': product.name, 'pk': product.pk, 'version': product.version}
                if product.factory_supplier is not None:
                    product_info['supplier'] = f'Factory {product.factory_supplier.name} no. ' \
                                               f'{product.factory_supplier.pk}'
                elif product.retailer_supplier is not None:
                    product_info['supplier'] = f'Retailer {product.retailer_supplier.name} no. ' \
                                               f'{product.retailer_supplier.pk}'
                elif product.entrepreneur_supplier is not None:
                    product_info['supplier'] = f'Entrepreneur {product.entrepreneur_supplier.name} no. ' \
                                               f'{product.entrepreneur_supplier.pk}'
                else:
                    product_info['supplier'] = ''

                output.append(product_info)

        return output

    def get_contacts(self, obj):
        return {'email': obj.email, 'country': obj.country, 'city': obj.city,
                'street': obj.country, 'house_number': obj.house_number}

    class Meta:
        model = Retailer
        exclude = ('owner', 'email', 'country', 'city', 'street', 'house_number')


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('owner', )

    def validate(self, attrs):
        factory_owner = attrs.get('factory_owner')
        entrepreneur_owner = attrs.get('entrepreneur_owner')
        retailer_owner = attrs.get('retailer_owner')

        factory_supplier = attrs.get('factory_supplier')
        entrepreneur_supplier = attrs.get('entrepreneur_supplier')
        retailer_supplier = attrs.get('retailer_supplier')

        if factory_supplier is not None:
            if entrepreneur_supplier is not None or retailer_supplier is not None:
                raise ValidationError('Невозможно указать более одного поставщика')
        elif entrepreneur_supplier is not None:
            if retailer_supplier is not None:
                raise ValidationError('Невозможно указать более одного поставщика')

        if factory_owner is not None:
            if entrepreneur_owner is not None or retailer_owner is not None:
                raise ValidationError('Невозможно указать более одного владельца')
        elif entrepreneur_owner is not None:
            if retailer_owner is not None:
                raise ValidationError('Невозможно указать более одного владельца')

        return super(ProductCreateSerializer, self).validate(attrs)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    company_owner = SerializerMethodField()
    supplier = SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('owner', 'factory_owner', 'retailer_owner', 'entrepreneur_owner',
                   'factory_supplier', 'retailer_supplier', 'entrepreneur_supplier', )

    def get_company_owner(self, obj):
        if obj.factory_owner is not None:
            return f'Factory {obj.factory_owner.name} no. {obj.factory_owner.pk}'
        elif obj.retailer_owner is not None:
            return f'Retailer {obj.retailer_owner.name} no. {obj.retailer_owner.pk}'
        elif obj.entrepreneur_owner is not None:
            return f'Entrepreneur {obj.entrepreneur_owner.name} no. {obj.entrepreneur_owner.pk}'
        else:
            return None

    def get_supplier(self, obj):
        if obj.factory_supplier is not None:
            return f'Factory {obj.factory_supplier.name} no. {obj.factory_supplier.pk}'
        elif obj.retailer_supplier is not None:
            return f'Retailer {obj.retailer_supplier.name} no. {obj.retailer_supplier.pk}'
        elif obj.entrepreneur_supplier is not None:
            return f'Entrepreneur {obj.entrepreneur_suppler.name} no. {obj.entrepreneur_supplier.pk}'
        else:
            return None
