from django.contrib import admin
from .models import Weapon, Type_of_weapon, Scope, Ammo, Type_of_ammo

# admin.site.register(Film)

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ['opis']
    list_display = ["name", "sell_price", "cal"]
    list_filter = ("sell_price", "cal")
    search_fields = ("name", "cal")

admin.site.register(Type_of_weapon)
admin.site.register(Scope)
admin.site.register(Ammo)
admin.site.register(Type_of_ammo)


