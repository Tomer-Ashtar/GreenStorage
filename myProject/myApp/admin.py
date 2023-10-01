from django.contrib import admin
from .models import workers
from .models import Equipment
from .models import Customer
from .models import SalesHistory
# Register your models here.
admin.site.register(Customer)
admin.site.register(Equipment)
admin.site.register(workers)
admin.site.register(SalesHistory)