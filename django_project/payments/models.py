from django.db import models
import uuid


class Item(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    price = models.FloatField(verbose_name="Цена")
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self) -> str:
        return f"Предмет {self.name}"

class Order(models.Model):
    items = models.ManyToManyField("Item")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        items_string = ", ".join([i.name for i in self.items.all()])
        return f"Заказ, включающий {items_string} предметы"

class Discount(models.Model):
    pass

class Tax(models.Model):
    pass