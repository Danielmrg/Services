from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Customer)

admin.site.register(Expert)

admin.site.register(Tag)

admin.site.register(Category)

admin.site.register(Request_srv)
