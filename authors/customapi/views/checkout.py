from oscarapi.views import checkout


class CheckoutView(checkout.CheckoutView):
    """
    Submit an order for checkout.

    POST(basket, shipping_address, [total, shipping_method_code, shipping_charge, billing_address])

    Example for Art-vostorg Store without registration:

    {
        "basket": "http://localhost:8000/api/baskets/56/",
        "guest_email": "foo@example.com",
        "shipping_address": {
            "country": "http://127.0.0.1:8000/api/countries/RU/",
            "first_name": "Михаил",
            "last_name": "Федоров",
            "line1": "ул. Советская, д.6",
            "line2": "",
            "notes": "Позвонить!!!!",
            "phone_number": "+79158663369",
            "state": "Москва"
        }
    }

    Default example:

    {
        "basket": "http://testserver/oscarapi/baskets/1/",
        "guest_email": "foo@example.com",
        "total": "100.0",
        "shipping_charge": {
            "currency": "EUR",
            "excl_tax": "10.0",
            "tax": "0.6"
        },
        "shipping_method_code": "no-shipping-required",
        "shipping_address": {
            "country": "http://127.0.0.1:8000/oscarapi/countries/NL/",
            "first_name": "Henk",
            "last_name": "Van den Heuvel",
            "line1": "Roemerlaan 44",
            "line2": "Kroekingen",
            "notes": "Niet STUK MAKEN OK!!!!",
            "phone_number": "+31 26 370 4887",
            "state": "Gerendrecht",
        }
        "billing_address": {
            "country": http://127.0.0.1:8000/oscarapi/countries/NL/,
            "first_name": "Jos",
            "last_name": "Henken",
            "line1": "Boerderijstraat 19",
            "line2": "",
            "line3": "",
            "line4": "Zwammerdam",
            "notes": "",
            "phone_number": "+31 27 112 9800",
            "postcode": "6666LL",
            "state": "Gerendrecht",
            "title": "Mr"
        }
    }

    returns the order object.
    """
    pass
