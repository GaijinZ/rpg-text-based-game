import random


class Hero:
    max_health = 60
    health = max_health
    max_mana = 30
    mana = max_mana
    gold = 100
    exp = 0
    lvl = 100
    level_up = 40
    spells = {}

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f'Jestem {self.name}, przybyłem by zabijać potwory i palić wiedźmy.'

    def sword_attack(self, enemy):
        self.mana += 5
        dmg = random.randint(4, 8)
        enemy.health -= dmg
        print(f'Atakujesz wroga za pomocą miecza za {dmg} punktów życia.\n')

    def has_spell(self, choose_spell):
        for key, value in self.spells.items():
            if choose_spell == key:
                return value
            print('Nie posiadasz takiego czaru')
            return False

    def spell_attack(self, enemy, spell_name):
        if spell_name.mana > self.mana:
            print('\nNie mie masz wystarczającej ilości many.\n')
            return False
        min_dmg = spell_name.min_dmg
        max_dmg = spell_name.max_dmg
        dmg = random.randint(min_dmg, max_dmg)
        self.mana -= spell_name.mana
        enemy.health -= dmg
        print(f'Atakujesz wroga za pomocą {spell_name} za {dmg} punktów życia.\n')
        return True

    def die(self):
        print('Stracileś wszystkie punkty życia. Nie żyjesz.\n')

    def lvl_up(self):
        if self.exp >= self.level_up:
            self.max_health += 5
            self.max_mana += 2
            self.lvl += 1
            self.level_up += 20
            return True
        return False

    def buy_spell(self, spell_name):
        for spell in spells_available.values():
            if spell_name in spell.name:
                if spell.gold_to_buy > self.gold:
                    print('\nNie masz hajsu.')
                    return False
                if spell.lvl > self.lvl:
                    print('\nPosiadasz za mały poziom doświadczenia. Idz bić potwory.\n')
                    return False
                self.gold -= spell.gold_to_buy
                self.spells[spell_name] = spell
                print(f'{spell} został dodany do Twoich czarów.\n')
                return self.spells
        print('\nNie ma takiego czaru')

    def show_skills(self):
        if not self.spells:
            print('Nie posiadasz nauczonych czarów')
            return False
        for spell, value in self.spells.items():
            print(f'{spell} obrażenia od {value.min_dmg} do {value.max_dmg},'
                  f' koszt many {value.mana} punktów many, typ obrażeń {value.dmg_type}.')

    def __str__(self):
        return self.name


class Monster:
    monster_name = None
    max_health = 0
    health = 0
    min_dmg = 0
    max_dmg = 0

    def attack(self, hero):
        dmg = random.randint(self.min_dmg, self.max_dmg)
        hero.health -= dmg
        print(f'Zostałeś zaatakowany za {dmg} punktów życia\n')

    def die(self):
        print('Zabiłeś potwora.\n')

    def get_exp_and_gold(self, hero):
        pass

    def __str__(self):
        return self.monster_name


class Rat(Monster):
    max_health = random.randint(10, 30)
    health = max_health
    min_dmg = 5
    max_dmg = 15

    def __init__(self, monster_name):
        super().__init__()
        self.monster_name = monster_name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(10, 15)
        gold_gained = random.randint(5, 12)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')


class Ogre(Monster):
    max_health = random.randint(20, 50)
    health = max_health
    min_dmg = 20
    max_dmg = 30

    def __init__(self, monster_name):
        super().__init__()
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
    min_dmg = 50
    max_dmg = 100

    def __init__(self, monster_name):
        super().__init__()
        self.monster_name = monster_name

    def get_exp_and_gold(self, hero):
        exp_gained = random.randint(20, 35)
        gold_gained = random.randint(12, 30)
        hero.exp += exp_gained
        hero.gold += gold_gained
        print(f'Zdobyłeś {exp_gained} punktów doświadczenia i {gold_gained} sztuk złota.\n')


class Spell:
    name = None
    dmg_type = None
    min_dmg = 0
    max_dmg = 0
    mana = 0
    gold_to_buy = 0
    lvl = 0

    def description(self):
        return f'{self.name} - obrażenia od {self.min_dmg} do {self.max_dmg}, '\
               f'koszt many {self.mana} punktów many, typ obrażeń {self.dmg_type}, '\
               f'koszt kupna {self.gold_to_buy} sztuk złota, '\
               f'wymagany poziom bohatera: {self.lvl}.'

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
    gold_to_buy = 5
    lvl = 1

    def additional_effect(self):
        effect = random.randrange(6)
        if effect == 1:
            self.max_dmg += 10
            print(f'\nSkuteczny atak {self.name}, przeciwnik staje w plomieniach. '
                  f'Maksymalne obrażenia zwiekszone o 10.')


class IceBolt(Spell):
    name = 'ice bolt'
    dmg_type = 'lód'
    min_dmg = 6
    max_dmg = 15
    mana = 7
    gold_to_buy = 10
    lvl = 3

    def additional_effect(self):
        effect = random.randrange(6)
        if effect == 1:
            self.mana += 10
            print(f'\nSkuteczny atak {self.name}, przeciwnik zamarza. '
                  f'Twoja mana została zregenerowana o 10 punktów.')


class Blizzard(Spell):
    name = 'blizzard'
    dmg_type = 'lód'
    min_dmg = 15
    max_dmg = 22
    mana = 10
    gold_to_buy = 15
    lvl = 5

    def additional_effect(self):
        effect = random.randrange(11)
        if effect == 1:
            self.max_dmg += 25
            print(f'\nSkuteczny atak {self.name}, przeciwnik zamarza. '
                  f'Twoja mana została zregenerowana o 25 punktów.')


class Earthquake(Spell):
    name = 'earthquake'
    dmg_type = 'ziemia'
    min_dmg = 25
    max_dmg = 30
    mana = 15
    gold_to_buy = 20
    lvl = 8

    def additional_effect(self):
        effect = random.randrange(6)
        if effect == 1:
            hero.health += 10
            print(f'\nSkuteczny atak {self.name}. Twoje zdrowie regeneruje się o 10 punktów życia.')


class Meteor(Spell):
    name = 'meteor'
    dmg_type = 'ogień'
    min_dmg = 30
    max_dmg = 40
    mana = 30
    gold_to_buy = 40
    lvl = 10

    def additional_effect(self):
        effect = random.randrange(11)
        if effect == 1:
            self.max_dmg += 25
            print(f'\nSkuteczny atak {self.name}, przeciwnik staje w płomieniach. '
                  f'Maksymalne obrażenia zwiekszone o 25.')


if __name__ == '__main__':
    print('\nWITAJ W GRZE ŚMIERTELNIKU\n')
    name = input("Wpisz imię bohatera: ")
    print('-' * 20 + '\n')

    hero = Hero(name)
    hero.say_hello()

    fireball = Fireball()
    ice_bolt = IceBolt()
    blizzard = Blizzard()
    earthquake = Earthquake()
    meteor = Meteor()

    spells_available = {'fireball': fireball,
                        'ice bolt': ice_bolt,
                        'blizzard': blizzard,
                        'earthquake': earthquake,
                        'meteor': meteor}

    print('Przemierzasz świat aby ratować wioski i zabijać potwory, które je nękają...\n')

    def shop():

        compare_spells = {k: v for (k, v) in spells_available.items() if k not in hero.spells}

        for spl in compare_spells.values():
            print(spl.description())

        while True:
            learn_spell = input('\nWpisz nazwę czaru, którego chcesz sie nauczyć '
                                'lub naciśnij ENTER, aby nie kupic żadnego czaru: ').lower()
            print('-' * 20 + '\n')
            if learn_spell == '':
                break
            if not hero.has_spell(learn_spell):
                if hero.buy_spell(learn_spell):
                    break
            print('Masz juź ten czar.\n')


    def fight():

        if hero.lvl <= 5:
            monster = Rat('szczur')
        elif 6 <= hero.lvl <= 9:
            monster = Ogre('ogr')
        else:
            monster = Troll('troll')

        print(f'Wędrując przez krainę natknąłeś się na ogromnego, brzydkiego {monster}a')

        while monster.health >= 0:
            print(f'\nMasz {hero.health} punktów życia i {hero.mana} punktów many.\n')
            print(f'Potwór posiada {monster.health} punktów życia.\n')

            while True:
                attack = int(input('Wybierz 1 jezeli chcesz zaatakować mieczem.\n'
                                   'Wybierz 2 jeżeli chesz zaatakować czarem\n'))
                if attack < 3:
                    break

            print('-' * 20 + '\n')
            if attack == 1:
                hero.sword_attack(monster)
            elif attack == 2:
                print('\nTwoje czary to:\n')
                hero.show_skills()
                choose_spell = input('\nWpisz nazwę czaru, którym chcesz zaatakować: ')
                print('-' * 20 + '\n')
                if hero.has_spell(choose_spell):
                    get_spell = hero.spells.get(choose_spell)
                    hero.spell_attack(monster, get_spell)
            if monster.health > 0:
                print('Potwór kontratakuje')
                monster.attack(hero)
            else:
                monster.die()
                monster.get_exp_and_gold(hero)
                hero.health = hero.max_health
                hero.mana = hero.max_mana
                print('Pijąc krew potwora uzupelniasz życia i manę.\n')
                print(f'Życie: {hero.health}, mana: {hero.mana}')
                if hero.lvl_up():
                    print(f'Awansujesz na poziom {hero.lvl}\n')
                    print(f'Twoje życie i mana zwiekszją się. Teraz wynoszą: {hero.max_health} i {hero.max_mana}\n')
        if hero.health <= 0:
            hero.die()

    while hero.health >= 0:

        fight()

        print(f'Posiadasz {hero.gold} sztuk złota.\n')
        go_to_shop = input('Wpisz "sklep" aby przejsc do sklepu.\n')
        print('-' * 20 + '\n')
        if go_to_shop == 'sklep':
            shop()
        continue
