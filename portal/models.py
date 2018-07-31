from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        blank=True
    )
    slug = models.SlugField(
        unique=True
    )
    parent = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        related_name='cat_child',
        on_delete=models.PROTECT
    )
    orden = models.IntegerField(
        null=True,
        blank=True
    )
    hidden = models.BooleanField(
        default=False
    )

    class Meta:
            verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=30,
        blank=True
    )
    slug = models.SlugField(
        unique=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )
    Categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='categories',
    )
    quantity = models.IntegerField(
        default=1

    )
    prince = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    short_description = models.CharField(
        max_length=255
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Inactive"
    )

    class meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class ProductQuestion(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT
    )
    question = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Inactive"
    )

class Meta:
    verbose_name_plural = "Questions"

def __str__(self):
    return self.question

class ProductAnswer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )
    product_question = models.ForeignKey(
        'ProductQuestion',
        on_delete=models.PROTECT
    )
    question = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    Status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Inactive"
    )

class Meta:
    verbose_name_plural = "Answers"

def __str__(self):
    return self.answer
