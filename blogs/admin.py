from django.contrib import admin
from .models import room
from .models import project
from .models import mail
# Register your models here.
admin.site.register(room)
admin.site.register(project)
admin.site.register(mail)

