from urllib import request

from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from account.permissions import IsActivePermission
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from django.http import Http404


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer = OrderSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    search_fields = ['title', 'order_info']
    
    permission_classes = [IsActivePermission]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return OrderCreateSerializer
        elif self.action == 'destroi':
            return [IsAdminUser()]
        return OrderSerializer

    @action(['GET'], detail=True)
    def reviews(self, request):
        orders = self.get_object()
        reviews = orders.reviews.all()
        serializer = OrderReviewSerializer(
            reviews, many=True
        )
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.data
        if data.get('title', False):
            instance.title = data.get('title')

        instance.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderReviewViewSet(ModelViewSet):
    queryset = OrderReview.objects.all()
    serializer_class = OrderReviewSerializer
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args,**kwargs)