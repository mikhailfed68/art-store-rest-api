from rest_framework import serializers
from oscarapi.serializers import product

from authors.customapi.services import get_product_price, get_product_availability


class ProductSerializer(product.ProductSerializer):
    product_class = serializers.StringRelatedField(read_only=True)
    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='painter-detail')
    price = serializers.SerializerMethodField()
    availability = serializers.SerializerMethodField()

    def get_price(self, obj):
        return get_product_price(self, obj)

    def get_availability(self, obj):
        return get_product_availability(self, obj)


class ProductLinkSerializer(product.ProductLinkSerializer):
    product_class = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    price = serializers.SerializerMethodField()
    availability = serializers.SerializerMethodField()

    def get_price(self, obj):
        return get_product_price(self, obj)

    def get_availability(self, obj):
        return get_product_availability(self, obj)
