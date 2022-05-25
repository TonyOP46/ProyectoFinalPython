from django.contrib import admin
from .models import Library, Rack, RackItem
# Register your models here.

admin.site.register(Library)
admin.site.register(Rack)
admin.site.register(RackItem)

