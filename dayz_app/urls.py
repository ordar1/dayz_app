from django.urls import path
from dayz_app.views import new_weapon, edit_weapon, delete_weapon, weapon_page, scope_page, edit_scope



urlpatterns = [
    path('new/', new_weapon, name="new_weapon"),
    path('edit/<int:id>/', edit_weapon, name="edit_weapon"),
    path('delete/<int:id>/', delete_weapon, name="delete_weapon"),
    path('weapon/<int:id>/', weapon_page, name="weapon_page"),
    path('scope/<int:id>/', scope_page, name="scope_page"),
    path('edit_scope/<int:id>/', edit_scope, name="edit_scope"),





]
