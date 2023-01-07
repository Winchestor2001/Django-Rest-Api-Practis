from django.db import models


class FoodCategory(models.Model):
    food_name = models.CharField(max_length=150)

    def __str__(self):
        return self.food_name


class Food(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    poster = models.ImageField(upload_to='food_img/', null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.category, self.name)


class TgUsers(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.user_id


class Order(models.Model):
    user = models.ForeignKey(TgUsers, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.food)
