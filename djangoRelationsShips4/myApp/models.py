from django.db import models

# Create your models here.

# Burada Multi Table Inheritance anlatılıyor.
class Place(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Bu modelde 'Place' modelini miras aldığımız için oradaki alanları bu model
# ile birlikte kullanabiliyoruz.
class Restaurant(Place):
    serves_pizza = models.BooleanField(default=False)
    serves_tuna = models.BooleanField(default=False)