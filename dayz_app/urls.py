from django.urls import path
from dayz_app.views import all_weapons, new_weapon, edit_weapon, delete_weapon, sniper_rifles, weapon_page, assault_rifles, shotguns, machine_guns, scope_page



urlpatterns = [
    path('wszystkie/', all_weapons, name="all_weapons"),
    path('new/', new_weapon, name="new_weapon"),
    path('edit/<int:id>/', edit_weapon, name="edit_weapon"),
    path('delete/<int:id>/', delete_weapon, name="delete_weapon"),
    path('sniperrifles/', sniper_rifles, name="sniper_rifles"),
    path('assaultrifles/', assault_rifles, name="assault_rifles"),
    path('shotguns/', shotguns, name="shotguns"),
    path('machine_guns/', machine_guns, name="machine_guns"),

    path('weapon/<int:id>/', weapon_page, name="weapon_page"),
    path('scope/<int:id>/', scope_page, name="scope_page"),




]
