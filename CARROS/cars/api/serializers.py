from rest_framework import serializers

from cars.models import Car, Brand, Color

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)  
    color = ColorSerializer(many=True, read_only=True)

    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)
    color_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Color.objects.all(), source='color', write_only=True)

    class Meta:
        model = Car
        fields = '__all__'