from django.db import models

# Create your models here.

# Burada eğer model'lerde aynı alanlar varsa bu ortak alanları tek bir model'de
# toplamak ve toplanan model'in diğer model'lerde miras alınması gösteriliyor.
# class Meta: abstract=True ile miras alınan modellere alanları ortak veriyor
# https://docs.djangoproject.com/en/3.1/topics/db/models/#model-inheritance

# Ortak alanların bulunduğu ana model
class ContactInfo(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    address = models.CharField(max_length=30)

    class Meta:
        abstract = True


# Ana model'i miras alan model
class Customer(ContactInfo):
    #name = models.CharField(max_length=40)
    #email = models.EmailField(max_length=40)
    #address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)


# Ana model'i miras alan model
class Staff(ContactInfo):
    #name = models.CharField(max_length=40)
    #email = models.EmailField(max_length=40)
    #address = models.CharField(max_length=30)
    position = models.CharField(max_length=30)