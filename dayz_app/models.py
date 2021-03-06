from django.db import models

class Type_of_ammo(models.Model):
    WIN = '.308'
    MOSIN = '7.62x54'
    SKS = '7.62x39'
    NATO = '5.56x45'
    AK74 = '5.45x39'
    SHOTGUN_AMMO = '12ga'
    REVOLVER = '.357'
    NINE_MIL = '9mm'
    LAPUA = '.338'
    CHEYTAC = '.408'
    BARRET = '.50'
    ACP_ROUND = '.45 ACP'

    CALIBER_CHOICES = [
        (WIN, '.308'),
        (MOSIN, '7.62x54'),
        (SKS, '7.62x39'),
        (NATO, '5.56x45'),
        (AK74, '5.45x39'),
        (SHOTGUN_AMMO, '12ga'),
        (REVOLVER, '.357'),
        (NINE_MIL, '9mm'),
        (LAPUA, '.338'),
        (CHEYTAC, '.408'),
        (BARRET, '.50'),
        (ACP_ROUND, '.45 ACP'),

    ]
    type = models.CharField(choices=CALIBER_CHOICES, max_length=60, blank=False, default='Caliber not defined')
    init_speed = models.PositiveSmallIntegerField(blank=False)
    health_damage = models.PositiveSmallIntegerField(blank=False)

    def __str__(self):
        return self.self_type()
    def self_type(self):
        return "{}".format(self.type)


class Type_of_weapon(models.Model):
    SNIPER = 'Sniper rifle'
    SHOTGUN = 'Shotgun'
    ASSAULT_RIFLE = 'Assault rifle'
    MACHINE_GUN = 'Machine gun'
    RIFLE = 'Rifle'
    PISTOL = 'Pistol'
    SUBMACHINE_GUN = 'Submachine gun'
    WEAPON_CHOICES = [
        (SNIPER, 'Sniper rifle'),
        (SHOTGUN, 'Shotgun'),
        (ASSAULT_RIFLE, 'Assault rifle'),
        (MACHINE_GUN, 'Machine gun'),
        (RIFLE, 'Rifle'),
        (PISTOL, 'Pistol'),
        (SUBMACHINE_GUN, 'Submachine gun')
    ]


    type = models.CharField(choices=WEAPON_CHOICES, max_length=60, blank=False,
                                   default='Weapon type not defined')


    def __str__(self):
        return self.name()
    def name(self):
        return "{}".format(self.type)

class Scope(models.Model):
        TWO = 'x2.5'
        THREE = 'x3'
        FOUR = 'x4'
        FIVE = 'x5'
        SIX = 'x6'
        SEVEN = 'x7'
        EIGHT = 'x8'
        TWELVE = 'x12'
        TWENTY_FIVE = 'x25'
        OTHER = 'Other'

        MAGNITUDE_CHOICES = [
            (TWO, 'x2.5'),
            (THREE, 'x3'),
            (FOUR, 'x4'),
            (FIVE, 'x5'),
            (SIX, 'x6'),
            (SEVEN, 'x7'),
            (EIGHT, 'x8'),
            (TWELVE, 'x12'),
            (TWENTY_FIVE, 'x25'),
            (OTHER, 'Other')

        ]

        name = models.CharField(max_length=64, blank=False, unique=True)
        magnitude = models.CharField(choices=MAGNITUDE_CHOICES, max_length=64, blank=False,
                                     default='Magnitude not defined')
        sell_price = models.PositiveIntegerField(blank=False)
        buy_price = models.PositiveIntegerField(blank=True, null=True, default="0")

        def __str__(self):
            return str(self.name_mag())

        def name_mag(self):
            return "{} ({})".format(self.name, self.magnitude)


class Weapon(models.Model):

    WIN = '.308'
    MOSIN = '7.62x54'
    SKS = '7.62x39'
    NATO = '5.56x45'
    AK74 = '5.45x39'
    SHOTGUN_AMMO = '12ga'
    REVOLVER = '.357'
    NINE_MIL = '9mm'
    LAPUA = '.338'
    CHEYTAC = '.408'
    BARRET = '.50'
    ACP_ROUND = '.45 ACP'

    CALIBER_CHOICES = [
        (WIN, '.308'),
        (MOSIN, '7.62x54'),
        (SKS, '7.62x39'),
        (NATO, '5.56x45'),
        (AK74, '5.45x39'),
        (SHOTGUN_AMMO, '12ga'),
        (REVOLVER, '.357'),
        (NINE_MIL, '9mm'),
        (LAPUA, '.338'),
        (CHEYTAC, '.408'),
        (BARRET, '.50'),
        (ACP_ROUND, '.45 ACP'),

    ]
    name = models.CharField(max_length=64, blank=False, unique=True)
    sell_price = models.PositiveIntegerField(blank=True, null=True, default="0")
    buy_price = models.PositiveIntegerField(blank=True, null=True, default="0")
    description = models.TextField(default="", blank=True)
    cal = models.CharField(choices=CALIBER_CHOICES, max_length=60, blank=False, default='Caliber not defined')
    picture = models.ImageField(upload_to="pictures", null=True, blank=True)
    additional = models.ForeignKey(Type_of_weapon, on_delete=models.CASCADE, null=True)
    scopes = models.ManyToManyField(Scope, related_name='weapon_scopes', blank=True, default='No scope provided')



    def __str__(self):
        return self.self_name()

    def self_name(self):
        return "{}".format(self.name)

class Ammo(models.Model):
    name = models.CharField(max_length=60, blank=False, default="Not provided")
    init_speed = models.PositiveSmallIntegerField(blank=False)
    health_damage = models.PositiveSmallIntegerField(blank=False)
    type = models.ForeignKey(Type_of_ammo, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.self_type()

    def self_type(self):
        return "{} ({})".format(self.name, self.type)
