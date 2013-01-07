from django.db import models
from books.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
	order_number = models.AutoField(primary_key=True)
	order_date = models.DateTimeField()
	buyer = models.ForeignKey(User)
	books = models.ManyToManyField(Book,through='OrderSpec')

class OrderSpec(models.Model):
	books = models.ForeignKey(Book)
	orders = models.ForeignKey(Order)
	quantity = models.IntegerField()
