from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])
    date_registered = models.DateTimeField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'



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
    year_of_release = models.DateField(verbose_name='Год выпуска')
    mileage = models.PositiveSmallIntegerField(default=0, null=True, blank=True, verbose_name='Пробег')
    the_body = models.CharField(max_length=100, null=True, blank=True, verbose_name='Кузов')
    colour = models.CharField(max_length=100, null=True, blank=True, verbose_name='Цвет')
    engine = models.CharField(max_length=100, null=True, blank=True, verbose_name='Двигатель')
    BOX_RU_CHOICES = [
        ('Механик', 'Механик'),
        ('Автомат', 'Автомат'),
    ]

    box_ru = models.CharField(max_length=100, choices=BOX_RU_CHOICES, verbose_name='Коробка', null=True, blank=True)

    DRIVE_RU_CHOICES = [
        ('полный', 'Полный'),
        ('задний', 'Задний'),
        ('Передний', 'Передний')
    ]

    drive_ru = models.CharField(max_length=100, choices=DRIVE_RU_CHOICES, verbose_name='Привод', null=True, blank=True)

    RUDDER_RU_CHOICES = [
        ('Левый', 'Левый'),
        ('Правый', 'Правый'),
    ]

    rudder_ru = models.CharField(max_length=10, choices=RUDDER_RU_CHOICES, verbose_name='Руль', null=True, blank=True)

    condition = models.CharField(max_length=100, null=True, blank=True, verbose_name='Состояние')
    customs = models.CharField(max_length=35, null=True, blank=True, verbose_name='Таможня')
    exchange = models.CharField(max_length=100, null=True, blank=True, verbose_name='Обмен')
    availability = models.BooleanField(verbose_name='Наличие')
    region_city_of_ale = models.CharField(max_length=35, verbose_name='Регион, город продажи')
    accounting = models.CharField(max_length=35, verbose_name='Учёт')
    other = models.TextField(null=True, blank=True, verbose_name='Прочее')
    price_dollars = models.PositiveSmallIntegerField()
    text = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)


    def price_som(self):
        price_som= self.price_dollars * 85
        return price_som

    def __str__(self):
        return f'{self.model}'

class CarPhotos(models.Model):
    model = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='car_images/')


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}-{self.car}'


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    car = models.ForeignKey(Car, related_name='reviews', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.car}'





