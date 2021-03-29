import random


class Spell:
    name = None
    dmg_type = None
    min_dmg = 0
    max_dmg = 0
    mana = 0
    gold_required = 0
    lvl_required = 0

    def description(self):
        return f'{self.name} - obrażenia od {self.min_dmg} do {self.max_dmg}, ' \
               f'koszt many {self.mana} punktów many, typ obrażeń {self.dmg_type}, ' \
               f'koszt kupna {self.gold_required} sztuk złota, ' \
               f'wymagany poziom bohatera: {self.lvl_required}.'

    def additional_effect(self):
        pass

    def __repr__(self):
        return self.name


class Fireball(Spell):
    name = 'fireball'
    dmg_type = 'ogień'
    min_dmg = 5
    max_dmg = 10
    mana = 5
    gold_required = 5
    lvl_required = 1

    def additional_effect(self):
        effect = random.randrange(6)
        if effect == 1:
            self.max_dmg += 10
            print(f'\nSkuteczny atak {self.name}, przeciwnik staje w plomieniach. '
                  'Maksymalne obrażenia zwiekszone o 10.')
            return self.max_dmg
        return False


class IceBolt(Spell):
    name = 'ice bolt'
    dmg_type = 'zimno'
    min_dmg = 6
    max_dmg = 15
    mana = 7
    gold_required = 10
    lvl_required = 3

    def additional_effect(self):
        effect = random.randrange(2)
        if effect == 1:
            print('\nSkuteczny atak, przeciwnik zamarza na jedna turę.')
        return False


class Blizzard(Spell):
    name = 'blizzard'
    dmg_type = 'zimno'
    min_dmg = 15
    max_dmg = 22
    mana = 10
    gold_required = 15
    lvl_required = 5

    def additional_effect(self):
        effect = random.randrange(11)
        if effect == 1:
            self.max_dmg += 25
            print(f'\nSkuteczny atak {self.name}, przeciwnik zamarza. '
                  'Maksymalne obrażenia zwiekszone o 25.')
            return self.max_dmg
        return False


class Earthquake(Spell):
    name = 'earthquake'
    dmg_type = 'ziemia'
    min_dmg = 25
    max_dmg = 30
    mana = 15
    gold_required = 20
    lvl_required = 8

    def additional_effect(self):
        effect = random.randrange(6)
        if effect == 1:
            self.min_dmg = self.max_dmg
            print(f'\nSkuteczny atak {self.name}. Zadajesz maksymalne obrażenia.')
            return self.min_dmg
        return False


class Meteor(Spell):
    name = 'meteor'
    dmg_type = 'ogień'
    min_dmg = 30
    max_dmg = 40
    mana = 30
    gold_required = 40
    lvl_required = 10

    def additional_effect(self):
        effect = random.randrange(11)
        if effect == 1:
            self.max_dmg += 25
            print(f'\nSkuteczny atak {self.name}, przeciwnik staje w płomieniach. '
                  f'Maksymalne obrażenia zwiekszone o 25.')
        return False


class HealingSpell(Spell):
    name = 'holy light'
    mana = 20
    gold_required = 30
    lvl_required = 5

    def description(self):
        return f'{self.name} - zupełnia całe życie, koszt many {self.mana}, ' \
               f'koszt kupna {self.gold_required} sztuk złota, ' \
               f'wymagany poziom bohatera: {self.lvl_required}.'


class Weapon:
    name = None
    min_dmg = 0
    max_dmg = 0
    gold_required = 0
    lvl_required = 0

    def description(self):
        return f'{self.name} - obrażenia od {self.min_dmg} do {self.max_dmg}, ' \
               f'koszt kupna {self.gold_required} sztuk złota, ' \
               f'wymagany poziom bohatera: {self.lvl_required}.'

    def __repr__(self):
        return self.name


class BaseWeapon(Weapon):
    name = 'rusty sword'
    min_dmg = 4
    max_dmg = 6
    gold_required = 0
    lvl_required = 1


class GiantSword(Weapon):
    name = 'giant sword'
    min_dmg = 5
    max_dmg = 8
    gold_required = 10
    lvl_required = 2


class LeviathanAxe(Weapon):
    name = 'leviathan axe'
    min_dmg = 8
    max_dmg = 12
    gold_required = 15
    lvl_required = 6


class WarScythe(Weapon):
    name = 'war scythe'
    min_dmg = 15
    max_dmg = 25
    gold_required = 25
    lvl_required = 10


class BladeOfChaos(Weapon):
    name = 'blade of chaos'
    min_dmg = 30
    max_dmg = 50
    gold_required = 50
    lvl_required = 15


class Armor:
    name = None
    health = 0
    defence = 0
    gold_required = 0
    lvl_required = 0

    def description(self):
        return f'{self.name} - zbroja dodaje do życia {self.health}, ' \
               f'zmniejszoneo obrażenia o {self.defence}.'

    def __repr__(self):
        return self.name


class MagePlate(Armor):
    name = 'mage plate'
    health = 10
    defence = 5
    gold_required = 15
    lvl_required = 5


class ArchonPlate(Armor):
    name = 'archon plate'
    health = 15
    defence = 10
    gold_required = 35
    lvl_required = 10


class HeavyPlate(Armor):
    name = 'heavy plate'
    health = 30
    defence = 15
    gold_required = 55
    lvl_required = 20


class Potion:
    name = None
    gold_required = 0
    lvl_required = 0
    action = ''

    def description(self):
        return f'{self.name} - {self.action}, ' \
               f'koszt kupna {self.gold_required} sztuk złota, ' \
               f'wymagany poziom bohatera: {self.lvl_required}'

    def __repr__(self):
        return self.name


class HealingPotion(Potion):
    name = 'zycia'
    gold_required = 5
    lvl_required = 1
    action = 'odnawia życie do pełna'


class ManaPotion(Potion):
    name = 'many'
    gold_required = 5
    lvl_required = 1
    action = 'odnawia manę do pełna'


class ReduceManaPotion(Potion):
    name = 'zmniejszona mana'
    gold_required = 8
    lvl_required = 3
    action = ' zmniejsza koszt rzucenia czaru o połowę'


class DoubleDmgPotion(Potion):
    name = 'podwojne obrazenia'
    gold_required = 12
    lvl_required = 5
    action = 'następny atak zada podwójne obrażenia'


class MaxDmgAndIgnoreImmunePotion(Potion):
    name = 'redukcja odpornosci'
    gold_required = 10
    lvl_required = 5
    action = 'usuwa odporność wroga, następny atak zada maksymalne obrażenia'


fireball = Fireball()
ice_bolt = IceBolt()
blizzard = Blizzard()
holy_light = HealingSpell()
earthquake = Earthquake()
meteor = Meteor()

giant_sword = GiantSword()
leviathan_axe = LeviathanAxe()
war_scythe = WarScythe()
blade_of_chaos = BladeOfChaos()

mage_plate = MagePlate()
archon_plate = ArchonPlate()
heavy_plate = HeavyPlate()

healing_potion = HealingPotion()
mana_potion = ManaPotion()
reduced_mana_potion = ReduceManaPotion()
double_dmg_potion = DoubleDmgPotion()
ignore_immune = MaxDmgAndIgnoreImmunePotion()

weapons_available = [giant_sword, leviathan_axe, war_scythe, blade_of_chaos]

spells_available = {'fireball': fireball,
                    'ice bolt': ice_bolt,
                    'blizzard': blizzard,
                    'holy light': holy_light,
                    'earthquake': earthquake,
                    'meteor': meteor}

armors_available = [mage_plate, archon_plate, heavy_plate]

potions_available = {'healing_potion': healing_potion,
                     'mana_potion': mana_potion,
                     'reduced_mana_potion': reduced_mana_potion,
                     'double_dmg_potion': double_dmg_potion,
                     'ignore_immune': ignore_immune}
