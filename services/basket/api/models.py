from django.db import models
from django.utils.translation import gettext_lazy as _


class BasketSession(models.Model):
    basket_id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=200)
    status_choices = [
        ('open', 'open'),
        ('closed', 'closed'),

    ]
    status = models.CharField(choices=status_choices, max_length=6)

    class Meta:
        ordering = ("basket_id",)
        verbose_name = _("BasketSession")
        verbose_name_plural = _("BasketSession")


class BasketItem(models.Model):
    basket_item_id = models.BigAutoField(primary_key=True)
    basket_session_id = models.ForeignKey(BasketSession, on_delete=models.CASCADE)
    catalog_item_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        ordering = ("catalog_item_id",)
        verbose_name = _("BasketItem")
        verbose_name_plural = _("BasketItem")
