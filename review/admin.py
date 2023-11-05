from django.contrib import admin

# Register your models here.
from .models import movies,userinputs
admin.site.register(movies)
admin.site.register(userinputs)

