from django.forms import ModelForm
from .models import Weapon, Scope
import django_filters

class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'buy_price', 'sell_price', 'cal', 'additional', 'scopes']


class ScopeForm(ModelForm):
    class Meta:
        model = Scope
        fields = ['name', 'magnitude']

"""
class WeaponFilterForm(django_filters.FilterSet):
    class Meta:
        model = Weapon
        fields = ['name']
"""

