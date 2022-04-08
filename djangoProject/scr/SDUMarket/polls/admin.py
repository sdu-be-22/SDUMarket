from django.contrib import admin


# Register your models here.


from .models import Payment


from .models import *

admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Card)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Profit)
admin.site.register(Order)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
