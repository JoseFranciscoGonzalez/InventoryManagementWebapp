from django.contrib import admin
from .models import Material, Trademark, System, MaterialHistory

# Register your models here.
admin.site.register(Trademark)
admin.site.register(System)
admin.site.register(MaterialHistory)

class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['description']
    readonly_fields = ['id']
    list_filter = ('system', 'trademark', 'status', 'owner')


class MaterialHistoryAdmin(admin.ModelAdmin):
    search_fields = ['material__description']
    list_filter = ('material__system',)


# Register the admin class with the associated model
admin.site.register(Material, MaterialAdmin)
admin.site.unregister(MaterialHistory)
admin.site.register(MaterialHistory, MaterialHistoryAdmin)
