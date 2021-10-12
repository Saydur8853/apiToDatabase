from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

#1 administator Model
class Administator(models.Model):
    name = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#2 Menu Model

class Menu(models.Model):
    administator = models.ForeignKey(Administator, on_delete=models.CASCADE)
    menuName = models.CharField(max_length=10)
    price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.menuName

#3 food Details model
class Food(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    specialItemId = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#Special Item
class SpecialItem(models.Model):
    menuName = models.CharField(max_length=100)
    food = models.OneToOneField(Food, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.menuName

#Most popular Item
 
class MostPopular(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#6 Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#5 Order Model
class Order(models.Model):
    orderDate = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    pickDate = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

#4 Order Item model
class OrderItem(models.Model):
    food = models.OneToOneField(Food, on_delete=models.CASCADE, primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=False)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    

#7 Payment Model

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    paymentDate = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    paymentType = models.CharField(max_length=50)
