import random


class Hero:
    LEVEL_UP = 40
    spells = []

    def __init__(self, name):
        self.name = name
        self.max_health = 60
        self.health = self.max_health
        self.max_mana = 30
        self.mana = self.max_mana
        self.gold = 5
        self.exp = 0
        self.lvl = 1

    def __str__(self):
        return f'\nJestem {self.name}, przybyłem by zabijać potwory i palić wiedźmy.'

    def sword_attack(self, enemy):
        self.mana += 5
        dmg = random.randint(5, 9)
        enemy.health -= dmg
        print(f'Atakujesz wroga za pomocą miecza za {dmg} punktów życia.\n')

    def spell_attack(self, enemy, spell_name):
        for spell in self.spells:
            if spell_name in spell.spell_name:
                if self.mana <= 0 or spell.mana > self.mana:
                    print('\nNie mie masz wystarczającej ilości many.\n')
                    return False
                min_dmg = spell.min_dmg
                max_dmg = spell.max_dmg
                dmg = random.randint(min_dmg, max_dmg)
                if spell.dmg_type == 'ogień':
                    addtional_dmg = random.randrange(6)
                    if addtional_dmg == 1:
                        dmg += 10
                        print('-' * 20)
                        print(f'\nSkuteczny atak {spell_name}, przeciwnik staje w plomieniach. '
                              f'Zadajesz dodatkowe 10 obrażeń')
                if spell.dmg_type == 'lód':
                    mana_recovery = random.randrange(6)
                    if mana_recovery == 1:
                        self.mana += 10
                        print('-' * 20)
                        print(f'\nSkuteczny atak {spell_name}, przeciwnik zamarza. '
                              f'Twoja mana została zregenerowana o 5 punktów.')
                if spell.dmg_type == 'ziemia':
                    dmg_recived = random.randrange(6)
                    if dmg_recived == 1:
                        self.health += 5
                        print('-' * 20)
                        print(f'\nSkuteczny atak {spell_name}. Twoje zdrowie regeneruje się o 5 punktów życia.')
                self.mana -= spell.mana
                enemy.health -= dmg
                print('-' * 20)
                print(f'Atakujesz wroga za pomocą {spell_name} za {dmg} punktów życia.\n')
                return True
        print('Nie posiadasz takiego czaru')
        return False

    def die(self):
        print('Stracileś wszystkie punkty życia. Nie żyjesz.\n')

    def level_up(self):
        if self.exp >= self.LEVEL_UP:
            self.max_health += 5
            self.max_mana += 2
            self.lvl += 1
            self.LEVEL_UP += 20
            return True
        return False

    def buy_spell(self, spell_name):
        for spell in spells_available:
            if spell_name in spell.spell_name:
                if spell.gold_to_buy > self.gold:
                    print('\nNie masz hajsu.')
                    return False
                if spell.lvl > self.lvl:
                    print('\nPosiadasz za mały poziom doświadczenia. Idz bić potwory.\n')
                    return False
                self.gold -= spell.gold_to_buy
                self.spells.append(spell)
                print(f'\n{spell} został dodany do Twoich czarów.')
                return self.spells
        print('\nNie ma takiego czaru')

    def show_skills(self):
        if not self.spells:
            print('Nie posiadasz nauczonych czarów')
        for skill in self.spells:
            print(f'{skill.spell_name} obrażenia od {skill.min_dmg} do {skill.max_dmg},'
                  f' koszt many {skill.mana} punktów many, typ obrażeń {skill.dmg_type}.')


class Monster:
    def __init__(self):
        self.monster_name = None
        self.max_health = 0
        self.health = 0
        self.dmg = 0

    def __str__(self):
        return self.monster_name

    def attack(self, hero):
        dmg = self.dmg
        hero.health -= dmg
        print(f'Zostałeś zaatakowany za {dmg} punktów życia\n')
        return dmg

    def die(self):
        print('Zabiłeś potwora.\n')


class Rat(Monster):
    def __init__(self, monster_name):
        super().__init__()
        self.monster_name = monster_name
        self.max_health = random.randint(10, 25)
        self.health = self.max_health
        self.dmg = random.randint(5, 15)


class Ogre(Monster):
    def __init__(self, monster_name):
        super().__init__()
        self.monster_name = monster_name
        self.max_health = random.randint(20, 50)
        self.health = self.max_health
        self.dmg = random.randint(20, 30)


class Troll(Monster):
    def __init__(self, monster_name):
        super().__init__()
        self.monster_name = monster_name
        self.max_health = random.randint(50, 100)
        self.health = self.max_health
        self.dmg = random.randint(50, 100)


class Spell:
    def __init__(self):
        self.spell_name = None
        self.dmg_type = None
        self.min_dmg = 0
        self.max_dmg = 0
        self.mana = 0
        self.gold_to_buy = 0
        self.lvl = 0

    def __str__(self):
        return self.spell_name

    def description(self):
        return f'{self.spell_name} - obrażenia od {self.min_dmg} do {self.max_dmg}, ' \
               f'koszt many {self.mana} punktów many, typ obrażeń {self.dmg_type}, ' \
               f'koszt kupna {self.gold_to_buy} sztuk złota, ' \
               f'wymagany poziom bohatera: {self.lvl}.'


class Fireball(Spell):
    def __init__(self, spell_name, dmg_type):
        super().__init__()
        self.spell_name = spell_name
        self.dmg_type = dmg_type
        self.min_dmg = 5
        self.max_dmg = 10
        self.mana = 5
        self.gold_to_buy = 5
        self.lvl = 1


class IceBolt(Spell):
    def __init__(self, spell_name, dmg_type):
        super().__init__()
        self.spell_name = spell_name
        self.dmg_type = dmg_type
        self.min_dmg = 6
        self.max_dmg = 15
        self.mana = 7
        self.gold_to_buy = 10
        self.lvl = 3


class Blizzard(Spell):
    def __init__(self, spell_name, dmg_type):
        super().__init__()
        self.spell_name = spell_name
        self.dmg_type = dmg_type
        self.min_dmg = 15
        self.max_dmg = 22
        self.mana = 10
        self.gold_to_buy = 15
        self.lvl = 5


class Earthquake(Spell):
    def __init__(self, spell_name, dmg_type):
        super().__init__()
        self.spell_name = spell_name
        self.dmg_type = dmg_type
        self.min_dmg = 25
        self.max_dmg = 30
        self.mana = 15
        self.gold_to_buy = 20
        self.lvl = 8


class Meteor(Spell):
    def __init__(self, spell_name, dmg_type):
        super().__init__()
        self.spell_name = spell_name
        self.dmg_type = dmg_type
        self.min_dmg = 30
        self.max_dmg = 40
        self.mana = 30
        self.gold_to_buy = 40
        self.lvl = 10


if __name__ == '__main__':
    print('\nWITAJ W GRZE ŚMIERTELNIKU\n')
    name = input("Wpisz imię bohatera: ")

    hero = Hero(name)
    print(hero)

    rat = Rat('szczur')
    ogre = Ogre('ogr')
    troll = Troll('troll')

    fireball = Fireball('fireball', 'ogień')
    ice_bolt = IceBolt('ice bolt', 'lód')
    blizzard = Blizzard('blizzard', 'lód')
    earthquake = Earthquake('earthquake', 'ziemia')
    meteor = Meteor('meteor', 'ogień')

    spells_available = [
        fireball,
        ice_bolt,
        blizzard,
        earthquake,
        meteor
    ]

    print('\nBudzisz się na mega kacu w karczmie, w ktorej spotykasz czarnoksiężnika.\n'
          'Oferuje Ci, że nauczy Cię czarów za okresloną zapłatą.\n'
          f'Posiadasz {hero.gold} sztuk złota. Oto czary, które może Cie nauczyć czarnoksięznik:\n')

    def shop():

        shop_spells = set(spells_available)
        hero_skills = set(hero.spells)
        spells_to_buy = shop_spells - hero_skills

        for spell in spells_to_buy:
            print(spell.description())

        while True:
            print('-' * 20)
            learn_spell = input('\nWpisz nazwę czaru, którego chcesz sie nauczyć '
                                'lub naciśnij ENTER, aby nie kupic żadnego czaru: ').lower()
            if learn_spell == '':
                break
            if hero.buy_spell(learn_spell):
                break

    def fight():

        if hero.lvl <= 5:
            monster = rat
            exp_gained = random.randint(10, 15)
            gold_gained = random.randint(5, 12)
        elif 6 <= hero.lvl <= 9:
            monster = ogre
            exp_gained = random.randint(10, 20)
            gold_gained = random.randint(5, 12)
        else:
            monster = troll
            exp_gained = random.randint(20, 35)
            gold_gained = random.randint(12, 30)

        monster.health = monster.max_health

        print(f'\nPrzemierzając krainę natknąłeś się na ogromnego, brzydkiego {monster}a\n')

        while monster.health >= 0:
            print('-' * 20)
            print(f'\nMasz {hero.health} punktów życia i {hero.mana} punktów many\n')
            print('-' * 20)
            attack = int(input('\nWybierz 1 jezeli chcesz zaatakować mieczem.\n'
                               'Wybierz 2 jeżeli chesz zaatakować czarem\n'))
            if attack == 1:
                hero.sword_attack(monster)
            elif attack == 2:
                print('\nTwoje czary to:\n')
                hero.show_skills()
                print('-' * 20)
                spell = input('\nWpisz nazwę czaru, którym chcesz zaatakować: ')
                hero.spell_attack(monster, spell)
            if monster.health > 0:
                print('Potwór kontratakuje')
                monster.attack(hero)
                print('-' * 20)
            else:
                monster.die()
                hero.exp += exp_gained
                hero.gold += gold_gained
                hero.health = hero.max_health
                hero.mana = hero.max_mana
                print('-' * 20)
                print(f'Zdobyłeś {exp_gained} doświadczenia i {gold_gained} sztuk złota.\n')
                print('Pijąc krew potwora uzupelniasz życia i manę.\n')
                print(f'Życie: {hero.health}, mana: {hero.mana}')
                print('-' * 20)
                if hero.level_up():
                    print(f'Awansujesz na poziom {hero.lvl}\n')
                    print(f'Twoje życie i mana zwiekszją się. Teraz wynoszą: {hero.max_health} i {hero.max_mana}\n')
        if hero.health <= 0:
            hero.die()
            print('-' * 20)

    while hero.health >= 0:
        shop()
        fight()

        print('-' * 20)
        print('Po walce masz szanse kupić nowy czar.\n')
        print(f'Posiadasz {hero.gold} sztuk złota.\n')
