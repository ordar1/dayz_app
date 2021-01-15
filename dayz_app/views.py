from django.shortcuts import render, get_object_or_404, redirect
from .models import Weapon, Scope
from .forms import WeaponForm, ScopeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from dayz_app.serializers import UserSerializer, GroupSerializer, ScopeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ScopeViewSet(viewsets.ModelViewSet):
    serializer_class = ScopeSerializer

    def get_queryset(self):
        scopes = Scope.objects.filter(name="PU-Scope")
        return scopes


def all_weapons(request):
    all = Weapon.objects.all()
    weapons = Weapon.objects.filter(additional_id=1)
    shotguns = Weapon.objects.filter(additional_id=2)
    machine_guns = Weapon.objects.filter(additional_id=3)
    assault_rifles = Weapon.objects.filter(additional_id=4)
    pistols = Weapon.objects.filter(additional_id=6)
    rifles = Weapon.objects.filter(additional_id=5)
    submachines = Weapon.objects.filter(additional_id=7)

    for weapon in weapons:
        weapon.filtered = Scope.objects.filter(weapon_scopes=weapon)

    for shotgun in shotguns:
        shotgun.filtered = Scope.objects.filter(weapon_scopes=shotgun)

    for machine_gun in machine_guns:
        machine_gun.filtered = Scope.objects.filter(weapon_scopes=machine_gun)

    for assault_rifle in assault_rifles:
        assault_rifle.filtered = Scope.objects.filter(weapon_scopes=assault_rifle)

    for pistol in pistols:
        pistol.filtered = Scope.objects.filter(weapon_scopes=pistol)

    for rifle in rifles:
        rifle.filtered = Scope.objects.filter(weapon_scopes=rifle)

    for submachine in submachines:
        submachine.filtered = Scope.objects.filter(weapon_scopes=submachine)

    return render(request, 'landing_page.html', {'weapons' : weapons, 'all': all, 'shotguns': shotguns, 'machine_guns': machine_guns, 'assault_rifles': assault_rifles,
                                          'pistols': pistols, 'rifles': rifles, 'submachines': submachines})

def new_weapon(request):
    form_weapon = WeaponForm(request.POST or None, request.FILES or None)

    if form_weapon.is_valid():
        form_weapon.save()
        return redirect(all_weapons)

    return render(request, 'weapon_form.html', {'form': form_weapon, 'new': True})

def edit_weapon(request, id):
    weapon = get_object_or_404(Weapon, pk=id)
    form_weapon = WeaponForm(request.POST or None, request.FILES or None, instance=weapon)

    if form_weapon.is_valid():
        weapon.save()
        return redirect(all_weapons)



    return render(request, 'weapon_form.html', {'form': form_weapon, 'new': False, 'weapon': weapon})

def edit_scope(request, id):
    scope = get_object_or_404(Scope, pk=id)
    form_scope = ScopeForm(request.POST or None, instance=scope)

    if form_scope.is_valid():
        scope.save()
        return redirect(all_weapons)

    return render(request, 'scope_form.html', {'form': form_scope, 'new': False})


@login_required
def delete_weapon(request, id):
    weapon = get_object_or_404(Weapon, pk=id)

    if request.method == "POST":
        weapon.delete()
        return redirect(all_weapons)

    return render(request, 'confirm.html', {'weapon': weapon})

def scope_page(request, id):
    scope = get_object_or_404(Scope, pk=id)
    all_weapons = Weapon.objects.filter(scopes=scope)
    for weapon in all_weapons:
        weapon.filtered = weapon

    return render(request, 'scope_page.html', {'scope': scope, 'all_weapons': all_weapons, 'weapon': weapon})

def weapon_page(request, id):
    weapon = get_object_or_404(Weapon, pk=id)
    all_scopes = Scope.objects.filter(weapon_scopes=weapon)
    for scope in all_scopes:
        scope.filtered = scope

    return render(request, 'weapon_page.html', {'weapon' : weapon, 'all_scopes' : all_scopes})
