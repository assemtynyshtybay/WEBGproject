from rest_framework import serializers
from api.models import Category,Image


class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)

    def create(self,validated_data):
        # category = Category.objects.create(name=validated_data.get('name'))
        category = Category.objects.create(**validated_data)
        return category
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance

class CategorySerializer2(serializers.ModelSerializer):
    class Meta():
        model = Category
        # fields = ('id',)
        fields = '__all__'
    #здесь он привязан к модельке category и
    # имеет доступ к его филдам, то есть может достать все его филды
    # required=True будет все по умолчанию, знает все типы
    # методы create,update уже за нас записаны

class ImageSerializer(serializers.ModelSerializer):
        # Nested Serializers
        price = serializers.IntegerField(required=False)
        category = CategorySerializer2(read_only=True)
        category_id = serializers.IntegerField(read_only=True)
        class Meta:
            model = Image
            fields = ('id', 'name', 'price','description','category','category_id',)

class CategoryWithVacanciesSerializer(serializers.ModelSerializer):
        # vacancies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # vacancies = serializers.StringRelatedField(many=True, read_only=True)
        vacancies = ImageSerializer(many=True, read_only=True)
        class Meta:
            model = Category
            fields = ('id', 'name', 'vacancies')