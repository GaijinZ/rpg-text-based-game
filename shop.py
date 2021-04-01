from spells import Fireball, IceBolt, Blizzard, Earthquake, Meteor, HealingSpell
from items import GiantSword, LeviathanAxe, WarScythe, BladeOfChaos, MagePlate, ArchonPlate, \
    HeavyPlate, HealingPotion, ManaPotion, ReduceManaPotion, DoubleDmgPotion, MaxDmgAndIgnoreImmunePotion

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
                'reduced mana potion': reduced_mana_potion,
                'double dmg potion': double_dmg_potion,
                'ignore immune': ignore_immune},
}
