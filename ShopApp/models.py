import uuid
from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, verbose_name="Ім'я")
    last_name = models.CharField(max_length=255, verbose_name="Прізвище")
    phone = models.CharField(max_length=20, verbose_name="Контактний телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата реєстрації")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Покупець"
        verbose_name_plural = "Покупці"
        db_table = 'shop_customers'


class Seller(models.Model):

    class Position(models.TextChoices):
        SELLER = 'SELLER', 'Продавець'
        SENIOR_SELLER = 'SENIOR', 'Головний продавець'
        HEAD_OF_SALES = 'HEAD', 'Керівник відділу продажів'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, verbose_name="Ім'я")
    last_name = models.CharField(max_length=255, verbose_name="Прізвище")
    phone = models.CharField(max_length=20, verbose_name="Контактний телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    hire_date = models.DateField(verbose_name="Дата працевлаштування")
    position = models.CharField(
        max_length=10,
        choices=Position.choices,
        default=Position.SELLER,
        verbose_name="Посада у фірмі"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.get_position_display()})"

    class Meta:
        verbose_name = "Продавець"
        verbose_name_plural = "Продавці"
        db_table = 'shop_sellers'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Назва товару")
    description = models.TextField(verbose_name="Опис товару", blank=True, null=True)

    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна товару")

    seller = models.ForeignKey(
        Seller,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name="Закріплений продавець"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        db_table = 'shop_products'


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='purchases',
        verbose_name="Покупець"
    )
    seller = models.ForeignKey(
        Seller,
        on_delete=models.PROTECT,
        related_name='sales',
        verbose_name="Продавець"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='sales_history',
        verbose_name="Товар"
    )

    sale_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажу")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість проданого товару")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума продажу")

    def __str__(self):
        return f"Продаж {self.id} від {self.sale_date.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name = "Продаж"
        verbose_name_plural = "Продажі"
        db_table = 'shop_sales'