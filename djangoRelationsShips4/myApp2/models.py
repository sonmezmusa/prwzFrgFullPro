from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Burada Proxy Model Inheritance gösteriliyor. Proxy'de miras alınan model'in
# özelliklerine(property) müdehale edebilirsin.
class MyUser(User):
    class Meta:
        ordering = ('username',)

        proxy = True

    def fullName(self):
        return self.first_name + ' ' + self.last_name



# Burada proxy metod'umuzun kullanılışı:
# >>> from myApp2.models import MyUser
# >>> u = MyUser.objects.all()[0]
# >>> u
# <MyUser: musa>
# >>> u.fullName()
# 'Musa Sönmez'

# Burada Django'nun metod'unun kullanılışı:
# >>> u2 = User.objects.all()[0]
# >>> u2.get_full_name()
# 'Musa Sönmez'

