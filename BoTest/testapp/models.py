from django.db import models


class Quadratic(models.Model):
    eq_id = models.AutoField(primary_key = True)
    a_value = models.FloatField(null=False, blank=False, max_length=16)
    b_value = models.FloatField(null=False, blank=False, max_length=16)
    c_value = models.FloatField(null=False, blank=False, max_length=16)
    result_1 = models.FloatField(null=True, blank=True, max_length=16)
    result_2 = models.FloatField(null=True, blank=True, max_length=16)
    objects = models.Manager()


class ColorsItems(models.Model):
    item_id = models.IntegerField(primary_key = True)
    color = models.CharField(max_length=16, null= False)
    objects = models.Manager()