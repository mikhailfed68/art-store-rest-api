from oscarapi.serializers import checkout


class OrderSerializer(checkout.OrderSerializer):
    lines = None
    