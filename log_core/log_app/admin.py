from django.contrib import admin
from .models import User,User_Role,Groups,Work_update

admin.site.register(User)
admin.site.register(User_Role)
# admin.site.register(Student)
admin.site.register(Groups)
admin.site.register(Work_update)
