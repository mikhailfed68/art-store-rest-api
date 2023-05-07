from rest_framework import serializers

from oscarapi.serializers import product


def get_product_price(self, obj):
    """
    Return price dictionary for product-list and prodcut-detail.
    This feature was implemented because the mixin concept doesn't work here.
    """
    if obj.stockrecords.exists():
        return {'currency': obj.stockrecords.first().price_currency, 'value': obj.stockrecords.first().price}
    return {'currency': None, 'value': None}    


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

    def get_price(self, obj):
        return get_product_price(self, obj)
