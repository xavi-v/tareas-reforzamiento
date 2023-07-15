from django.contrib import admin
from django.contrib.auth.models import User, Permission

# Register your models here.

from .models import Task
#admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","description")

admin.site.unregister(User) # importante

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "puede_crear_tarea", "last_login", "date_joined" )
    @admin.display(boolean=True)
    def puede_crear_tarea(self, obj):
        return obj.has_perm("listar.add_Task")

