from django.db import models


class CatalogItem(models.Model):
    catalog_item_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    price = models.FloatField
    quantity = models.IntegerField
    stars_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
         ('4', '4'),
         ('5', '5'),
    ]
    stars = models.CharField(choices=stars_choices, max_length = 1)
    
   
    def __str__(self):
        return self.title


class Opinion(models.Model):
    opinion_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(CatalogItem, on_delete=models.CASCADE)
   # user_id = models.ForeignKey(CatalogItem, on_delete=models.CASCADE)
    text = models.CharField(max_length = 500)
    stars_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
         ('4', '4'),
         ('5', '5'),
    ]
    stars = models.CharField(choices=stars_choices, max_length = 1)
    
   
