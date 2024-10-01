from django.contrib import admin

# Register your models here.
from lng_volumes.models import LNGVolume, Country


class LNGVolumeAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(model_or_iterable=LNGVolume, admin_class=LNGVolumeAdmin)
admin.site.register(model_or_iterable=Country, admin_class=CountryAdmin)
