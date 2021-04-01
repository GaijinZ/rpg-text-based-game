import random


class Monster:
    monster_name = None
    max_health = 0
    health = 0
    min_dmg = 0
    max_dmg = 0
    dmg_done = 0
    immune = None

    def attack(self):
        self.dmg_done = random.randint(self.min_dmg, self.max_dmg)
        return self.dmg_done

    def hit(self, hero):
        self.dmg_done -= hero.defence
        hero.health -= self.dmg_done
        print(f'Potwór kontratakuje za {self.dmg_done} obrażeń')

    def die(self):
        print('Zabiłeś potwora.\n')

    def get_exp_and_gold(self, hero):
        pass

    def has_immune(self, spell_name, hero):
        if spell_name.dmg_type == self.immune:
            hero.mana -= spell_name.mana
            return True

    def __str__(self):
        return self.monster_name


class Rat(Monster):
    max_health = random.randint(15, 25)
    health = max_health
    min_dmg = 5
    max_dmg = 15
    immune = 'ogień'

    def __init__(self, monster_name):
        self.monster_name = monster_name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(10, 15)
        gold_gained = random.randint(5, 12)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')


class Ogre(Monster):
    max_health = random.randint(30, 60)
    health = max_health
    min_dmg = 20
    max_dmg = 30
    dmg_done = 0
    immune = 'zimno'

    def __init__(self, monster_name):
        self.monster_name = monster_name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(10, 20)
        gold_gained = random.randint(5, 12)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')


class Troll(Monster):
    max_health = random.randint(50, 100)
    health = max_health
    min_dmg = 40
    max_dmg = 80
    immune = 'ogień'

    def __init__(self, monster_name):
        self.monster_name = monster_name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(20, 35)
        gold_gained = random.randint(12, 30)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')
