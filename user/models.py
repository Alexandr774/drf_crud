from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
     verbose_name = "Локация"
     verbose_name_plural = "Локации"

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=9, blank=True)
    age = models.PositiveSmallIntegerField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользоваьтель'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name



class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveSmallIntegerField()
    description = models.TextField()
    is_published = models.BinaryField(default=False)
    image = models.ImageField(upload_to='avito/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
     verbose_name = "Объявление"
     verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name








