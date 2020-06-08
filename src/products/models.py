from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
    featured = models.BooleanField(default=False)

    def get_product_list_url(self):
        return reverse("products:product_list")

    def get_product_update_url(self):
        return reverse("products:product_update", kwargs={'product_id': self.id})

    def get_product_delete_url(self):
        return reverse("products:product_delete", kwargs={'product_id': self.id})
