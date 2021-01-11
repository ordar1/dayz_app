from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Weapon, Type_of_weapon, Scope, Ammo
from .forms import WeaponForm, ScopeForm
from django.contrib.auth.decorators import login_required



def all_weapons(request):
    wszystkie = Weapon.objects.all()
    weapons = Weapon.objects.filter(additional_id=1)
    shotguns = Weapon.objects.filter(additional_id=2)
    machine_guns = Weapon.objects.filter(additional_id=3)
    assault_rifles = Weapon.objects.filter(additional_id=4)
    pistols = Weapon.objects.filter(additional_id=6)
    rifles = Weapon.objects.filter(additional_id=5)
    submachines = Weapon.objects.filter(additional_id=7)
    ammos = Ammo.objects.all()
    for weapon in weapons:
        weapon.ming = Scope.objects.filter(weapon_scopes=weapon)
        scopes = Scope.objects.filter(weapon_scopes=weapon)

    for shotgun in shotguns:
        shotgun.ming = Scope.objects.filter(weapon_scopes=shotgun)

    for machine_gun in machine_guns:
        machine_gun.ming = Scope.objects.filter(weapon_scopes=machine_gun)

    for assault_rifle in assault_rifles:
        assault_rifle.ming = Scope.objects.filter(weapon_scopes=assault_rifle)

    for pistol in pistols:
        pistol.ming = Scope.objects.filter(weapon_scopes=pistol)

    for rifle in rifles:
        rifle.ming = Scope.objects.filter(weapon_scopes=rifle)

    for submachine in submachines:
        submachine.ming = Scope.objects.filter(weapon_scopes=submachine)

    for ammo in ammos:
        ammo.single = ammo

    return render(request, 'filmy.html', {'weapons' : weapons, 'wszystkie': wszystkie, 'scopes': scopes, 'shotguns': shotguns, 'machine_guns': machine_guns, 'assault_rifles': assault_rifles,
                                          'pistols': pistols, 'rifles': rifles, 'submachines': submachines, 'ammos': ammos})

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



    return render(request, 'weapon_form.html', {'form': form_weapon, 'new': False})

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

def landing_page(request):
    return render(request, 'landing_page.html')

def sniper_rifles(request):
    weapons = Weapon.objects.filter(additional_id=1)
    for weapon in weapons:
        weapon.ming = Scope.objects.filter(weapon_scopes=weapon)
        scopes = Scope.objects.filter(weapon_scopes=weapon)

    return render(request, 'sniper_rifles.html', {'weapons': weapons, 'scopes': scopes})

def scope_page(request, id):
    scope = get_object_or_404(Scope, pk=id)
    print(scope)
    all_weapons = Weapon.objects.filter(scopes=scope)
    print(all_weapons)
    for weapon in all_weapons:
        print(weapon)

    return render(request, 'scope_page.html', {'scope': scope, 'all_weapons': all_weapons, 'weapon': weapon})

def shotguns(request):
    weapons = Weapon.objects.filter(additional_id=2)
    for weapon in weapons:
        weapon.ming = Scope.objects.filter(weapon_scopes=weapon)
        scopes = Scope.objects.filter(weapon_scopes=weapon)

    return render(request, 'shotguns.html', {'weapons': weapons, 'scopes': scopes})

def assault_rifles(request):
    weapons = Weapon.objects.filter(additional_id=3)
    return render(request, 'assault_rifles.html', {'weapons': weapons})

def machine_guns(request):
    weapons = Weapon.objects.filter(additional_id=4)
    return render(request, 'machine_guns.html', {'weapons': weapons})



def weapon_page(request, id):
    weapon = get_object_or_404(Weapon, pk=id)
    all_scopes = Scope.objects.filter(weapon_scopes=weapon)
    for scope in all_scopes:
        print(scope)

    return render(request, 'weapon_page.html', {'weapon' : weapon, 'all_scopes' : all_scopes})

"""def new_weapon(request):
    form_weapon = WeaponForm(request.POST or None, request.FILES or None)
    form_type_of_weapon = type_of_weaponForm(request.POST or None)

    if all((form_weapon.is_valid(),form_type_of_weapon.is_valid())):
        weapon = form_weapon.save(commit=False)
        type_of_weapon = form_type_of_weapon.save()
        weapon.type_of_weapon = type_of_weapon
        weapon.save()

        return redirect(all_weapons)

    return render(request, 'weapon_form.html', {'form': form_weapon, 'new': True, 'form_type_of_weapon':  form_type_of_weapon})
weapon_scopes = weapon.scopes.all()
ID DLA PRZYPOMNIENIA: Assault rifles = 18, Machine Gun = 17, Shotgun = 16, Sniper rifles = 15"""
