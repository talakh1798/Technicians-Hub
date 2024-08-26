from django.contrib import admin
from Technicians_app.models import Technician, User, Review, Role, Admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


# Register your models
admin.site.register(Technician)
admin.site.register(Review)
admin.site.register(Role)
admin.site.register(Admin)

# Register User with your custom UserAdmin class
admin.site.register(User, CustomUserAdmin)

