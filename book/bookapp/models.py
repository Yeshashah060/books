from django.db import models

# Create your models here.
class books(models.Model):
	bname = models.CharField(max_length=50)

	bauthor = models.CharField(max_length=50)

	bprice = models.IntegerField()

	def __str__(self):
		return self.bname