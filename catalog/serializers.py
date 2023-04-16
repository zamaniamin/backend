from rest_framework import serializers
from .models import Variant, VariantItem


# class VariantItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VariantItem
#         fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    # variant_items = VariantItemSerializer(many=True)
    #
    class Meta:
        model = Variant
        fields = '__all__'
    #     fields = ('id', 'product', 'name', 'variant_items')
    #
    # def create(self, validated_data):
    #     variant_items_data = validated_data.pop('variant_items')
    #     variant = Variant.objects.create(**validated_data)
    #     for item in variant_items_data:
    #         VariantItem.objects.create(variant=variant, **item)
    #     return variant
