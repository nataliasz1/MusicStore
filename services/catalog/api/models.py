from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


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
        return reverse("catalog_service:category_id", args=[self.slug])

    def __str__(self):
        return self.name


class CatalogItem(models.Model):
    catalog_item_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, blank=True)
    description_long = models.TextField(null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stars_choices = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    stars = models.IntegerField(choices=stars_choices, default=0)

    class Meta:
        ordering = ("price",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    """ def save(self, *args, **kwargs):
        self.slug = self.name + '' + self.catalog_item_id
        super(CatalogItem, self).save(*args, **kwargs)
 """


class Opinion(models.Model):
    opinion_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(CatalogItem, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    stars_choices = [

        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    stars = models.IntegerField(choices=stars_choices)


class ProductImage(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    catalog_item_id = models.ForeignKey(CatalogItem, related_name='images', on_delete=models.CASCADE)
    file = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image {self.image_id} for {self.catalog_item_id.name}'
