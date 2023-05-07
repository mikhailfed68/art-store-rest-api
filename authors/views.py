from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from authors.models import Painter
from authors.serializers import PainterDetailSerializer, PainterListSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'basket': reverse('api-basket', request=request, format=format),
        'basket/add-product': reverse('api-basket-add-product', request=request, format=format),
        'basket/add-voucher': reverse('api-basket-add-voucher', request=request, format=format),
        'basket/shipping-methods': reverse('api-basket-shipping-methods', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'checkout': reverse('api-checkout', request=request, format=format),
        'countries': reverse('country-list', request=request, format=format),
        'painters': reverse('painter-list', request=request, format=format),
    })


class PainterListView(generics.ListAPIView):
    queryset = Painter.objects.all()
    serializer_class = PainterListSerializer


class PainterDetailView(generics.RetrieveAPIView):
    queryset = Painter.objects.all()
    serializer_class = PainterDetailSerializer
