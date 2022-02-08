from rest_framework import serializers
from .models import Order, OrderReview


class OrderSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False),
                                   write_only=True, required=False)

    class Meta:
        model = Order
        fields = '__all__'



class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['title']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderReviewSerializer(serializers.ModelSerializer):
    orders_title = serializers.SerializerMethodField("get_orders_title")

    class Meta:
        model = OrderReview
        fields = '__all__'

    def get_orders_title(self, orders_review):
        title = orders_review.order.title
        return title

    def validate_news(self, reviews):
        if self.Meta.model.objects.filter(reviews=reviews).exists():
            raise serializers.ValidationError(
                "Вы уже оставляли коммент на этот заказ"
            )
        return reviews

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['name'] = user
        review = OrderReview.objects.create(**validated_data)
        return review




