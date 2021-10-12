from django.contrib import admin

# Register your models here.
from.models import Administator, Menu, Food, SpecialItem, MostPopular, Customer, Order, OrderItem, Payment
admin.site.register(Administator)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(SpecialItem)
admin.site.register(MostPopular)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)