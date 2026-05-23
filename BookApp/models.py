import uuid
from django.db import models


class Reader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=17)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        db_table = 'library_readers'


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Назва товару")
    author = models.CharField(max_length=255, verbose_name="Автор")
    regdate = models.DateTimeField()
    genre = models.TextField()
    publishing = models.TextField()
    is_taken = models.BooleanField(default=False)

    reader = models.ForeignKey(
        Reader,
        on_delete=models.PROTECT,
        related_name='books',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'library_books'
