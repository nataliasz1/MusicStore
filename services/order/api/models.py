from django.db import models


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    STATUS_CHOICES = (
        ("0", "created"),
        ("1", "completed"),
        ("2", "pending payment"),
        ("3", "failed"),
        ("4", "canceled"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='0')
    user_id = models.PositiveIntegerField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    catalog_item_id = models.PositiveIntegerField(null=False)
    quantity = models.PositiveIntegerField(null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return 'PK:%d, catalog_item_id: %d, quantity: %d, price: %.2f' % (
        self.order_item_id, self.catalog_item_id, self.quantity, self.price)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("0", "pending"),
        ("1", "received"),
        ("2", "failed"),
        ("3", "canceled"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='0')

    def __str__(self):
        return 'PK:%d, status: %s, user_id: %d' % (self.payment_id, self.STATUS_CHOICES[int(self.status)], self.user_id)
