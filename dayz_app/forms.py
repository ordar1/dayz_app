from django.forms import ModelForm
from .models import Weapon, Scope

class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'buy_price', 'sell_price', 'cal', 'additional', 'scopes']


class ScopeForm(ModelForm):
    class Meta:
        model = Scope
        fields = ['name', 'magnitude', 'sell_price', 'buy_price']

