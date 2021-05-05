from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _



class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class CatalogItem(models.Model):
    catalog_item_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    price = models.FloatField()
    quantity = models.IntegerField()
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    stars_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
         ('4', '4'),
         ('5', '5'),
    ]
    stars = models.CharField(choices=stars_choices, max_length = 1)
    
   
    class Meta:
        ordering = ("price",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])


    def __str__(self):
        return self.name


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
    
   
