from django.contrib import admin
from .models import *
class CommnutiyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Post)
admin.site.register(Communities, CommnutiyAdmin)
