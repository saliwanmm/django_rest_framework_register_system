from rest_framework import serializers

from .models import ProductsModel


class ProductsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductsModel
        # fields = ("title", "content", "category")
        fields = "__all__"