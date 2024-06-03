from django.db import models
from django.contrib.auth.models import User


class ProductsModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey("CategoryModel", on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.name