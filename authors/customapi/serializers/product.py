from rest_framework import serializers
from oscarapi.serializers import product
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from authors.customapi.services import get_product_price


class ProductImageListSerializer(product.ProductImageSerializer):
    """Returns hyperlinked scaled and cached image for Product images."""
    original_for_list = HyperlinkedSorlImageField('x550',  options={"crop": "center"}, source='original')


class ProductSerializer(product.ProductSerializer):
    product_class = serializers.StringRelatedField(read_only=True)
    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='painter-detail')
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return get_product_price(self, obj)


class ProductLinkSerializer(product.ProductLinkSerializer):
    product_class = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    price = serializers.SerializerMethodField()
    images = ProductImageListSerializer(many=True, required=False)

    def get_price(self, obj):
        return get_product_price(self, obj)
