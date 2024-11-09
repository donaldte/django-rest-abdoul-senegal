from rest_framework import serializers 
from produits.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Category
        fields = '__all__'
        
    # def validate_name(self, value): #clean_fieldname
    #     liste_mots_interdits = ['cat', 'dog', 'mouse']
    #     if value in liste_mots_interdits:
    #         raise serializers.ValidationError(f"Name cannot be {value}")
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name must be at least 3 characters long")
    #     return value
    
    
    # def validate(self, attrs):
    #     if attrs['name'] == 'cat':
    #         raise serializers.ValidationError("Name cannot be cat")
    #     return super().validate(attrs)
    
    
    def create(self, validated_data):
        email = validated_data.pop('email')
        print('-----------------', email)
        return super().create(validated_data)
    
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    