from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=80)
	

class Publisher(models.Model):
	name = models.CharField(max_length=100)
	office = models.CharField(max_length =100)
	phone = models.IntegerField()

class Book(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	quantity = models.IntegerField()
	author= models.ManyToManyField(Author)
	publisher = models.ManyToManyField(Publisher)

