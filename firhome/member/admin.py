from django.contrib import admin
from .models import User ,Wine, manwine

admin.site.register(User)
# Register your models here.
admin.site.register(Wine)
admin.site.register(manwine)
