class ReplenishLifeEffect:
    turns = 1

    def potion_effect(self, hero,monster):
        hero.health = hero.max_health
        return hero.health


class ReplenishManaEffect:
    turns = 1

    def potion_effect(self, hero, monster):
        hero.mana = hero.max_mana
        return hero.mana


class DoubleDmgEffect:
    turns = 2

    def potion_effect(self, hero, monster):
        hero.dmg_to_make *= 2
        hero.potion_choice = None
        return hero.dmg_to_make


class MaxDmgAndIgnoreImmunePotionEffect:
    turns = 3

    def potion_effect(self, hero, monster):
        monster.immune = None
        hero.dmg_done = hero.weapon.max_dmg
        hero.potion_choice = None
        return monster.immune, hero.dmg_done


effect_to_make = {
    'hp': ReplenishLifeEffect(),
    'mp': ReplenishManaEffect(),
    'dd pot': DoubleDmgEffect(),
    'ii pot': MaxDmgAndIgnoreImmunePotionEffect()
}