from django.db import models

class Marka(models.Model):
    marka_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.marka_name

class Model(models.Model):
    marka = models.ForeignKey(Marka, related_name='model', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name

class Car(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year_of_release = models.DateField()
    mileage = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    the_body = models.CharField(max_length=100, null=True, blank=True)
    colour = models.CharField(max_length=100, null=True, blank=True)
    engine = models.CharField(max_length=100, null=True, blank=True)
    BOX_CHOICES = [
        ('Механик', 'Механик'),
        ('Автомат', 'Автомат'),
    ]
    box = models.CharField(max_length=100, choices=BOX_CHOICES)
    DRIVE_CHOICES = [
        ('полный', 'Полный'),
        ('задний', 'Задний'),
        ('Передний', 'Передний')
    ]
    drive = models.CharField(max_length=100, choices=DRIVE_CHOICES)
    RUDDER_CHOICES = [
        ('Левый', 'Левый'),
        ('Правый', 'Правый'),
    ]
    rudder = models.CharField(max_length=10)





