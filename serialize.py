from rest_framework import serializers 
from project.models import Supplier,User,Medicine,Order

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id',
                  'name',
                  'email',
                  'phone',
                  'address')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'email',
                  'phone',
                  'address')

class MedicineSerializer(serializers.ModelSerializer):
    content = serializers.JSONField()
    class Meta:
        model = Medicine
        fields = (  'id',
                    'name',
                    'content',
                    'category',
                    'expDate',
                    'price',
                    'supplier',
                    'stock')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( 'id',
                    'ordDate',
                    'userId',
                    'medId',
                    'quantity',
                    'price'
        )
