from oscar.apps.partner.strategy import Selector


# This functions was implemented because the mixin concept doesn't work here.
def get_product_price(self, product):
    """Return price dictionary for product-list and prodcut-detail."""
    strategy = Selector().strategy()
    info = strategy.fetch_for_product(product).price
    return dict(
        currency=info.currency,
        incl_tax=info.incl_tax
    )


def get_product_availability(self, product):
    """Return availability dictionary for product-list and prodcut-detail."""
    strategy = Selector().strategy()
    info = strategy.fetch_for_product(product).availability
    return dict(
        is_available_to_buy=info.is_available_to_buy,
        num_available=info.num_available,
        message=info.message
    )
