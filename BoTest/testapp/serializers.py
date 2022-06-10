
from rest_framework import serializers
from .models import *


class QuadraticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadratic
        fields = ['a_value', 'b_value', 'c_value', 'result_1', 'result_2']


class ColorsItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorsItems
        fields = ['item_id', 'color']