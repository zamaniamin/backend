from rest_framework import generics
from .serializers import VariantSerializer
from .models import Variant, VariantItem


class AddVariantView(generics.CreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class VariantListView(generics.CreateAPIView):
    model = Variant
    serializer_class = VariantSerializer

# class AddVariantItemView(generics.CreateAPIView):
#     queryset = VariantItem.objects.all()
#     serializer_class = VariantItemSerializer
