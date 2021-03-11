from django.contrib import admin

# Register your models here.
from reservations_management.models import Reservations, ReservedProducts, ReservationRange , ReservationTasks

admin.site.register(Reservations)
admin.site.register(ReservedProducts)
admin.site.register(ReservationRange)
admin.site.register(ReservationTasks)