from django.db import models

# Create your models here.
from django.db.models import CharField, DecimalField, DateField


class BookInfo(models.Model):
    book_name = CharField(max_length=20)
    book_privce = DecimalField(max_digits=5, decimal_places=2)
    book_date = DateField()

    def __str__(self):
        return self.book_name


class HeroInfo(models.Model):
    hname = CharField(max_length=20)
    #性别 说明是bool类型，是一个男性
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.hname