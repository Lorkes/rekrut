from django.contrib import admin
from .models import User, Cat, Hunting


class CatAdmin(admin.ModelAdmin):
    readonly_fields = ('cat_sex',)


admin.site.register(User)
admin.site.register(Cat, CatAdmin)
admin.site.register(Hunting)
