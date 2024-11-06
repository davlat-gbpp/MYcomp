from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=127)
    price = models.FloatField()
    description = models.CharField(max_length=2048)
    category = models.CharField(max_length=32) 
    """category привязана к категориям товара и его характеристикам"""

"""Характеристики разной техники"""
class LoptopCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    display = models.CharField(max_length=16)
    cpu = models.CharField(max_length=32)
    gpu = models.CharField(max_length=32)
    ram = models.CharField(max_length=32)
    disk = models.CharField(max_length=64)
    os = models.CharField(max_length=16)
    keyboard_language = models.CharField(max_length=32)
    fk_product = models.ForeignKey()

class PCCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    cpu = models.CharField(max_length=32)
    gpu = models.CharField(max_length=32)
    ram = models.CharField(max_length=32)
    disk = models.CharField(max_length=64)
    os = models.CharField(max_length=16)
    connection = models.CharField(max_length=16)
    fk_product = models.ForeignKey()

class MonitorCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    size = models.FloatField() 
    display = models.CharField()
    frame_rate = models.IntegerField()    
    fk_product = models.ForeignKey()

class KeyboardCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    connection = models.CharField(max_length=16)
    cable_length = models.FloatField()
    keyboard_language = models.CharField(max_length=32)
    fk_product = models.ForeignKey()

class MouseCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    sensor = models.CharField()
    connection = models.CharField(max_length=16)
    cable_length = models.FloatField()
    fk_product = models.ForeignKey()
   
class MicrophoneCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    mic_type = models.CharField()
    frequency_min = models.IntegerField()
    frequency_max = models.IntegerField()
    connection = models.CharField(max_length=16)
    cable_length = models.FloatField()
    fk_product = models.ForeignKey()
    
class HeadphonesCharacteristics(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=16)
    noise_reduction = models.BooleanField(default=False)
    frequency_min = models.IntegerField()
    frequency_max = models.IntegerField()
    connection = models.CharField(max_length=16)
    cable_length = models.FloatField()
    fk_product = models.ForeignKey()
    
