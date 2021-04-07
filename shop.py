from spells import Fireball, IceBolt, Blizzard, Earthquake, Meteor, HealingSpell
from items import GiantSword, LeviathanAxe, WarScythe, BladeOfChaos, MagePlate, ArchonPlate, \
    HeavyPlate, HealingPotion, ManaPotion, DoubleDmgPotion, MaxDmgAndIgnoreImmunePotion
from enemy import Rat, Ogre, Troll

giant_sword = GiantSword()
leviathan_axe = LeviathanAxe()
war_scythe = WarScythe()
blade_of_chaos = BladeOfChaos()

mage_plate = MagePlate()
archon_plate = ArchonPlate()
heavy_plate = HeavyPlate()

healing_potion = HealingPotion()
mana_potion = ManaPotion()
double_dmg_potion = DoubleDmgPotion()
ignore_immune = MaxDmgAndIgnoreImmunePotion()

fireball = Fireball()
ice_bolt = IceBolt()
blizzard = Blizzard()
holy_light = HealingSpell()
earthquake = Earthquake()
meteor = Meteor()

items_to_buy = {
    'weapons': {'giant sword': giant_sword,
                'leviathan axe': leviathan_axe,
                'war scythe': war_scythe,
                'blade of chaos': blade_of_chaos},
    'armors': {'mage plate': mage_plate,
               'archon plate': archon_plate,
               'heavy plate': heavy_plate},
    'spells': {'fireball': fireball,
               'ice bolt': ice_bolt,
               'blizzard': blizzard,
               'holy light': holy_light,
               'earthquake': earthquake,
               'meteor': meteor},
    'potions': {'healing potion': healing_potion,
                'mana potion': mana_potion,
                'double dmg potion': double_dmg_potion,
                'ignore immune': ignore_immune},
}

monsters = {
    'rat': Rat(),
    'ogre': Ogre(),
    'troll': Troll(),
}


def monster_info():
    for monster_info in monsters.values():
        print(monster_info.bestiary())


def items_to_view():
    for key, value in items_to_buy.items():
        print(f'\n{key}\n')
        for items in value.values():
            print(items.description())


def purchase_items(hero):
    while True:
        spells_effects = input(
            '\nAby dowiedzieć się więcej o dodatkowych efektach czarów wpisz "efekty",'
            ' wciśnij ENTER aby przejśc dalej ').lower()

        if spells_effects == 'efekty':
            for i in items_to_buy['spells'].values():
                print(i.additional_effect_info)

        item_category_to_buy = input('\nWpisz kategorię przedmiotu: ').lower()
        item_name_to_buy = input('\nWpisz nazwę przedmiotu, który chcesz kupić: ').lower()
        print('-' * 20 + '\n')

        if item_name_to_buy == '':
            return False
        item_name = items_to_buy.get(item_category_to_buy).get(item_name_to_buy)
        if item_name_to_buy != str(item_name):
            print('\nNie ma takiego przedmiotu.\n')
            break
        if hero.has_gold_lvl_required(item_name):
            hero.buy_from_shop(item_name)
            if item_category_to_buy != 'potions':
                del items_to_buy[item_category_to_buy][item_name_to_buy]
            print(f'{item_name_to_buy} został dodany do Twoich przedmiotów.\n')
            break
