from rest_framework import serializers
from oscarapi.serializers import checkout
from oscar.apps.partner.strategy import Selector
from oscar.core.loading import get_model

Line = get_model('basket', 'line')
Basket = get_model('basket', 'basket')


class OrderSerializer(checkout.OrderSerializer):
    lines = None


class CheckoutSerializer(checkout.CheckoutSerializer):
    def validate_basket(self, value):
        basket = Basket.objects.get(id=value.id)
        strategy = Selector().strategy()

        for line in basket.all_lines():
            availability = strategy.fetch_for_line(line).availability
            if not availability.is_available_to_buy:
                raise serializers.ValidationError(f'Товар "{line.product}" распродан')
            if availability.num_available < line.quantity:
                raise serializers.ValidationError(f'{line.quantity} шт. товара {line.product} недоступно, осталось {availability.num_available}')
        return value
