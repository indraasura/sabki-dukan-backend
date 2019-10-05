from django.db import models
from django.urls import reverse
from django. conf import settings
import uuid

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Product(models.Model): #blogpost_set -> access qs with fk
	p_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
	title = models.CharField(max_length=120)#max_length is required
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	image = models.ImageField(upload_to="media/", max_length=254, blank=True, null=True)
	stock = models.IntegerField()
	
	def __str__(self):
		return "%s"%(self.p_id)


from django.core.validators import RegexValidator
import random

'''
class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = 
'''

class PhoneUser(models.Model):
	phone_id = models.AutoField(primary_key=True)
	phone_regex = RegexValidator(regex=r'\d{10}$', message="Phone number must be entered in the format: '+9999999999' ")
	phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
	otp = models.IntegerField( default = random.randint(10000, 99999) )

	def __str__(self):
		return "%s"%(self.phone_id)

class Transactions(models.Model):
	trans_id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
	fk_p_id = models.ForeignKey(Product, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	quantity = models.IntegerField(default=1)
	fk_phone = models.ForeignKey(PhoneUser, null=True, on_delete = models.CASCADE)

class ReceiptModel(models.Model):
	receipt_id = models.UUIDField(default=uuid.uuid4, primary_key = True, editable = False)
	price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
	order_id = models.CharField(blank=True, max_length = 100)#vo dega
	payment_id = models.CharField(blank=True, max_length=100)#vo dega






