import random
from enum import Enum


class Immune(Enum):
    FIRE = 1
    COLD = 2


class Monster:
    name = None
    min_health = 0
    max_health = 0
    health = random.randint(min_health, max_health)
    current_health = health
    min_dmg = 0
    max_dmg = 0
    dmg_done = 0
    immune = None
    type = None
    occurs = None
    frozen = 0

    def bestiary(self):
        return f'{self.name} - maksymalne życie {self.max_health}, obrażenia od {self.min_dmg} '\
               f'do {self.max_dmg}, odporność na {self.immune.keys()}, pojawia się: {self.occurs}.\n'

    def monster_type(self, hero):
        if hero.lvl <= 5:
            self.type = Rat('Szczur')
        elif 6 <= hero.lvl <= 15:
            self.type = Ogre('Ogr')
        else:
            self.type = Troll('Troll')
        return self.type

    def boss(self):
        self.type.min_health *= 2
        self.type.max_health *= 2
        self.type.current_health = self.type.health
        self.type.min_dmg *= 2
        self.type.max_dmg *= 2
        print(f'Trafiasz na zmutowany gatunek {self.type.name}a,który posiada zwiekszone życie i obrażenia.\n'
              'Bądź ostrożny.\n')
        return True

    def attack(self):
        self.dmg_done = random.randint(self.min_dmg, self.max_dmg)
        return self.dmg_done

    def hit(self, hero):
        self.dmg_done -= hero.defence
        hero.health -= self.dmg_done
        print(f'Potwór kontratakuje za {self.dmg_done} obrażeń\n')

    def die(self):
        print('Zabiłeś potwora.\n')

    def get_exp_and_gold(self, hero):
        pass

    def has_immune(self, spell_name, hero):
        if spell_name.dmg_type == self.immune:
            hero.mana -= spell_name.mana
            return True

    def __str__(self):
        return self.name


class Rat(Monster):
    min_health = 15
    max_health = 25
    health = random.randint(min_health, max_health)
    current_health = health
    health = max_health
    min_dmg = 5
    max_dmg = 15
    occurs = 'lasy'
    immune = Immune.COLD

    def __init__(self, name):
        self.name = name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(10, 15)
        gold_gained = random.randint(5, 12)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')


class Ogre(Monster):
    min_health = 30
    max_health = 60
    health = random.randint(min_health, max_health)
    current_health = health
    min_dmg = 20
    max_dmg = 30
    dmg_done = 0
    occurs = 'bagna'
    immune = Immune.FIRE

    def __init__(self, name):
        self.name = name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(10, 20)
        gold_gained = random.randint(5, 12)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')


class Troll(Monster):
    min_health = 50
    max_health = 100
    health = random.randint(min_health, max_health)
    current_health = health
    min_dmg = 40
    max_dmg = 80
    occurs = 'jaskinie'
    immune = Immune.FIRE

    def __init__(self, name):
        self.name = name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(20, 35)
        gold_gained = random.randint(12, 30)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')
