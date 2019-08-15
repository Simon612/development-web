from django.contrib import admin
from .models import Text, MainText, lists, Emails
# Register your models here.

admin.site.register(Text)
admin.site.register(MainText)
admin.site.register(lists)
admin.site.register(Emails)