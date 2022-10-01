from django.db import models

# Create your models here.


class Account(models.Model):
   customerID = models.AutoField(primary_key=True)
   username = models.CharField(max_length=40)
   password = models.CharField(max_length=30)
   regNo = models.CharField(max_length=9)
   Block = models.CharField(max_length=2)
   Gender = models.CharField(max_length=1, choices=(('M', 'Male'),('F', 'Female')))
   roomNo = models.IntegerField()
   phoneNo = models.IntegerField()
   email = models.EmailField()

   class Meta:
        verbose_name_plural = "Accounts"

class Orders(models.Model):
   orderID = models.AutoField(primary_key=True)
   customerID = models.ForeignKey(Account, on_delete=models.CASCADE)
   status = models.CharField(max_length=1, choices=(('A', 'Approved'),('P', 'Pending')))
   Restaurant = models.CharField(max_length=20,default="default store") 
   received = models.CharField(max_length=1, choices = (('t','True'),('f','False')))
   

   def __str__(self):
      return self.name

   class Meta:
        verbose_name_plural = "Orders"   

class OrderDetails(models.Model):
   orderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
   item = models.CharField(max_length=20)
   quantity = models.IntegerField()
   priceForEach = models.IntegerField()

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Order Details"   

class Stores(models.Model):
   storeID = models.AutoField(primary_key=True)
   storeName = models.CharField(max_length=30)
   storeDesc = models.CharField(max_length=200)
   image = models.ImageField(upload_to=None)

   def __str__(self):
      return self.storeName
   
   class Meta:
      verbose_name_plural = "Stores"   

class StoreMenu(models.Model):
   storeID = models.ForeignKey(Stores, on_delete=models.CASCADE)
   item = models.CharField(max_length=20)
   image = models.ImageField(upload_to=None)
   category = models.CharField(max_length=20)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Store Menu"   

class OffersCarousel(models.Model):
   image = models.ImageField(upload_to=None)




