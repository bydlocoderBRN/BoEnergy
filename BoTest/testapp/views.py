from django.shortcuts import render

from rest_framework import views

from rest_framework import request

from .serializers import *

from django.db import models

from rest_framework import response, status

from .models import *

from .service import *

class QuadroView(views.APIView):

    def get(self,request: request.Request):
        params = request.query_params
        a = params.get('a_value')
        b = params.get('b_value')
        c = params.get('c_value')
        if check_float(a) and check_float(b) and check_float(c):
            a_val = float(a)
            b_val = float(b)
            c_val = float(c)
            filtered_qs:models.QuerySet = Quadratic.objects.filter(a_value__exact= a_val, b_value__exact = b_val, c_value__exact=c_val)
            filtered_obj = list(filtered_qs)
            if len(filtered_obj) == 0:
                result = quad(a_val,b_val,c_val)
                quad_obj_new = Quadratic()
                quad_obj_new.a_value=a_val
                quad_obj_new.b_value=b_val
                quad_obj_new.c_value=c_val
                quad_obj_new.result_1=result.pop()
                quad_obj_new.result_2=result.pop()
                quad_obj_new.save()
                return response.Response(QuadraticSerializer(quad_obj_new).data,
                                         status.HTTP_200_OK)
            else:
                one_quad:Quadratic = filtered_obj.pop()
                return response.Response(QuadraticSerializer(one_quad).data,
                                         status.HTTP_200_OK)
        else: return response.Response("Вы ввели не число", status.HTTP_400_BAD_REQUEST)
        # serialized_data = QuadraticSerializer(data=raw_data)
        # if serialized_data.is_valid():
        #     result_data = serialized_data.validated_data
        #
        #     result = Quadratic.objects.filter(a_value__exact= result_data['a_value'], b_value__exact = result_data['b_value'], c_value__exact = result_data['c_value'])
        #     if result is not None:
        #         resp = 'первый корень ' + str(result['result_1']) + 'второй корень ' + str(result['result_2'])
        #         return response.Response(data=resp, status=status.HTTP_200_OK)
        #     else:
        #         res = quad(result_data['a_value'], result_data['b_value'], result_data['c_value'])
        #
        #         return response.Response("первый "+ str(res.pop()) + "второй " + str(res.pop()))


class ColorsView(views.APIView):

    def get(self, request, num):
        if num<=100:
            items_list = list(ColorsItems.objects.filter(item_id__exact=num))
            if len(items_list)!=0:
                return response.Response(ColorsItemsSerializer(items_list.pop()).data,status.HTTP_200_OK)
            else:
                item_new = ColorsItems()
                item_new.item_id = num
                item_new.color = getColor()
                item_new.save()
                return response.Response(ColorsItemsSerializer(item_new).data,status.HTTP_200_OK)
        else:
            return response.Response("Номер объекта превышает максимально допустимый", status.HTTP_400_BAD_REQUEST)
