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


class RustedSword(Weapon):
    name = 'rusted sword'
    min_dmg = 5
    max_dmg = 7
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

    def use_potion(self, hero, monster):
        pass

    def __repr__(self):
        return self.name


class HealingPotion(Potion):
    name = 'healing potion'
    gold_required = 5
    lvl_required = 1
    action = 'odnawia życie do pełna'


class ManaPotion(Potion):
    name = 'mana potion'
    gold_required = 5
    lvl_required = 1
    action = 'odnawia manę do pełna'


class DoubleDmgPotion(Potion):
    name = 'double dmg potion'
    gold_required = 12
    lvl_required = 5
    action = 'następny atak zada podwójne obrażenia'

    def use_potion(self, hero, monster):
        hero.dmg_to_make *= 2
        hero.potion_choice = None


class MaxDmgAndIgnoreImmunePotion(Potion):
    name = 'ignore immune'
    gold_required = 15
    lvl_required = 5
    action = 'usuwa odporność wroga, następny atak zada maksymalne obrażenia'

    def use_potion(self, hero, monster):
        monster.immune = None
        hero.dmg_done = hero.weapon.max_dmg
        hero.potion_choice = None


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

armors_available = [mage_plate, archon_plate, heavy_plate]

potions_available = {'healing_potion': healing_potion,
                     'mana_potion': mana_potion,
                     'reduced_mana_potion': reduced_mana_potion,
                     'double_dmg_potion': double_dmg_potion,
                     'ignore_immune': ignore_immune}
