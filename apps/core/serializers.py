from rest_framework import serializers
from apps.core.models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock', 'in_stock'
        ]
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")  
        return value
    


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'sub_total']



class OrderSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username')
    user_email = serializers.CharField(source='user.email')
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')
    total_price_without_method_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['order_id', 'status', 'user_username', 'user_email', 'created_at', 'items', 'total_price', 'total_price_without_method_name']
    
    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.sub_total for order_item in order_items)
    
    def get_total_price_without_method_name(self, obj):
        order_items = obj.items.all()
        return sum(order_item.sub_total for order_item in order_items)
    