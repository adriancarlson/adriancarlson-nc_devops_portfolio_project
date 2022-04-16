from django.contrib import admin

# Register your models here.
from .models import Parishes, Intentions, Meetings

admin.site.register(Parishes)
admin.site.register(Intentions)
admin.site.register(Meetings)
