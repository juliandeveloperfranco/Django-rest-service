from django.db import models


class Category(models.Model):
    description = models.CharField(
        max_length=50,
        help_text='Category description',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text="Description for subCategory"
    )

    def __str__(self):
        return '{}:{}'.format(self.category.description, self.description)

    class Meta:
        verbose_name_plural = 'SubCategories'
        unique_together = ('category', 'description')


class Product(models.Model):
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text='Product Description',
        unique=True
    )
    created_date = models.DateTimeField()
    selled = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = 'Products'
