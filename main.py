import random


class Hero:
    max_health = 500
    health = max_health
    max_mana = 30
    mana = max_mana
    base_weapon_dmg = 0
    base_spell_dmg = 0
    gold = 100
    exp = 0
    lvl = 6
    level_up = 25

    armor = []
    weapon = []
    spells = {}
    attributes = {'strength': 0, 'intelligence': 0, 'stamina': 0}

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Jestem {self.name}, przybyłem by zabijać potwory i palić wiedźmy.\n')

    def get_basic_weapon(self):
        return self.weapon.append(base_weapon)

    def sword_attack(self, enemy):
        if self.mana >= self.max_mana:
            self.mana = self.max_mana
        self.mana += 5
        weapon_attack = self.weapon[0]
        weapon_dmg = random.randint(weapon_attack.min_dmg, weapon_attack.max_dmg)
        dmg_done = weapon_dmg + self.base_weapon_dmg
        enemy.health -= dmg_done
        print(f'Atakujesz wroga za pomocą miecza za {dmg_done} punktów życia.\n')

    def has_spell_potion(self, item_group, item_name):
        if item_group == spells_available:
            item_group = self.spells
        for key, value in item_group.items():
            if item_name == key:
                return value

    def has_weapon_armor(self, item_group, item_name):
        if item_group == weapons_available:
            item_group = self.weapon
        elif item_group == armors_available:
            item_group = self.armor
        for item in item_group:
            if item_name == item.name:
                return True
            item_group.pop(0)
            return False

    def buy_weapon_armor(self, item_group, item_name):
        for item in item_group:
            if item_group == weapons_available:
                item_group = self.weapon
            elif item_group == armors_available:
                item_group = self.armor
            if item_name in item.name:
                if item.gold_required > self.gold:
                    print('\nNie masz hajsu.')
                    return False
                if item.lvl_required > self.lvl:
                    print('\nPosiadasz za mały poziom doświadczenia. Idz bić potwory.\n')
                    return False
                self.gold -= item.gold_required
                item_group.append(item)
                print(f'{item} został dodany do Twojego ekwipunku.\n')
                return True

    def buy_spell_potion(self, item_group, item_name):
        for i in item_group.values():
            if item_group == spells_available:
                item_group = self.spells
            if item_name in i.name:
                if i.gold_required > self.gold:
                    print('\nNie masz hajsu.')
                    return False
                if i.lvl_required > self.lvl:
                    print('\nPosiadasz za mały poziom doświadczenia. Idz bić potwory.\n')
                    return False
                self.gold -= i.gold_required
                item_group[item_name] = i
                print(f'{i} został dodany do Twojego ekwipunku.\n')
                return True

    def has_spell(self, choose_spell):
        for key, value in self.spells.items():
            if choose_spell == key:
                return value

    def spell_attack(self, enemy, spell_name):
        if spell_name.mana > self.mana:
            print('\nNie mie masz wystarczającej ilości many.\n')
            return False
        if spell_name == holy_light:
            self.mana -= spell_name.mana
            self.health = self.max_health
            print('Uzupełiasz życie.\n')
            return True
        self.mana -= spell_name.mana
        min_dmg = spell_name.min_dmg
        max_dmg = spell_name.max_dmg
        spell_dmg = random.randint(min_dmg, max_dmg)
        dmg_done = spell_dmg + self.base_spell_dmg
        enemy.health -= dmg_done
        print(f'Atakujesz wroga za pomocą {spell_name} za {dmg_done} punktów życia.\n')

    def has_armor(self):
        return self.armor

    def armor_defence(self, monster):
        for arm in self.armor:
            arm.health += self.max_health
            arm.less_dmg -= monster.dmg

    def die(self):
        print('Stracileś wszystkie punkty życia. Nie żyjesz.\n')

    def lvl_up(self):
        if self.exp >= self.level_up:
            self.max_health += 3
            self.max_mana += 2
            self.lvl += 1
            self.level_up *= 1.4
            return True
        return False

    def spend_points(self):
        print('Dostajesz 2 punkty do rozdania do swoich atrbutów.\n'
              '\nAtrybuty odpowiadają za:\n'
              'Siła - obrażeniaod broni\n'
              'Inteligencja - obrażenia od czarów\n'
              'Stamina - maksymalne życie\n')
        print('Aktualnie posiadasz:\n')
        for key, value in self.attributes.items():
            print(f'{key} - {value}\n')
        points_to_spend = 2
        while points_to_spend != 0:
            points = input('Wpisz "sila", "inteligencja" lub "stamina" aby dodać punkt w wybrany atrybut.\n')
            if points == 'sila':
                self.attributes['strength'] += 1
                self.base_weapon_dmg += 2
                points_to_spend -= 1
                print('Dodajesz punkt w siłę.\n')
            elif points == 'inteligencja':
                self.attributes['intelligence'] += 1
                self.base_spell_dmg += 2
                points_to_spend -= 1
                print('Dodajesz punkt w inteligencję.\n')
            elif points == 'stamina':
                self.attributes['stamina'] += 1
                points_to_spend -= 1
                self.max_health += 2
                print('Dodajesz punkt w staminę.\n')
            else:
                print('Nie posiadasz takiego atrubutu.\n')

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
    dmg = 0

    def attack(self, hero):
        dmg = random.randint(self.min_dmg, self.max_dmg)
        hero.health -= dmg
        print(f'Zostałeś zaatakowany za {dmg} punktów życia\n')
        return dmg

    def die(self):
        print('Zabiłeś potwora.\n')

    def get_exp_and_gold(self, hero):
        pass

    def __str__(self):
        return self.monster_name


class Rat(Monster):
    max_health = random.randint(15, 25)
    health = max_health
    min_dmg = 5
    max_dmg = 15
    dmg = 0

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
    dmg = 0

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
    min_dmg = 40
    max_dmg = 80
    dmg = 0

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
                  f'Maksymalne obrażenia zwiekszone o 10.')


class IceBolt(Spell):
    name = 'ice bolt'
    dmg_type = 'lód'
    min_dmg = 6
    max_dmg = 15
    mana = 7
    gold_required = 10
    lvl_required = 3

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
    gold_required = 15
    lvl_required = 5

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
    gold_required = 20
    lvl_required = 8

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
    gold_required = 40
    lvl_required = 10

    def additional_effect(self):
        effect = random.randrange(11)
        if effect == 1:
            self.max_dmg += 25
            print(f'\nSkuteczny atak {self.name}, przeciwnik staje w płomieniach. '
                  f'Maksymalne obrażenia zwiekszone o 25.')


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
    less_dmg = 0
    gold_required = 0
    lvl_required = 0

    def description(self):
        return f'{self.name} - zbroja dodaje do życia {self.health}, ' \
               f'zmniejszoneo obrażenia o {self.less_dmg}.'

    def __repr__(self):
        return self.name


class MagePlate(Armor):
    name = 'mage plate'
    health = 10
    less_dmg = 5
    gold_required = 15
    lvl_required = 5


class ArchonPlate(Armor):
    name = 'archon plate'
    health = 15
    less_dmg = 10
    gold_required = 35
    lvl_required = 10


class HeavyPlate(Armor):
    name = 'heavy plate'
    health = 30
    less_dmg = 15
    gold_required = 55
    lvl_required = 20


class Potion:
    pass


class ReduceManaPotion(Potion):
    pass


class DoubleDmgPotion(Potion):
    pass


class HealingPotion(Potion):
    pass


class ManaPotion(Potion):
    pass


class MaxDmgAndIgnoreImmunePotion(Potion):
    pass


if __name__ == '__main__':
    print('\nWITAJ W GRZE ŚMIERTELNIKU\n')
    name = input("Wpisz imię bohatera: ")
    print('-' * 20 + '\n')

    hero = Hero(name)
    hero.say_hello()

    fireball = Fireball()
    ice_bolt = IceBolt()
    blizzard = Blizzard()
    holy_light = HealingSpell()
    earthquake = Earthquake()
    meteor = Meteor()

    base_weapon = BaseWeapon()
    giant_sword = GiantSword()
    leviathan_axe = LeviathanAxe()
    war_scythe = WarScythe()
    blade_of_chaos = BladeOfChaos()

    mage_plate = MagePlate()
    archon_plate = ArchonPlate()
    heavy_plate = HeavyPlate()

    weapons_available = [giant_sword, leviathan_axe, war_scythe, blade_of_chaos]

    spells_available = {'fireball': fireball,
                        'ice bolt': ice_bolt,
                        'blizzard': blizzard,
                        'holy light': holy_light,
                        'earthquake': earthquake,
                        'meteor': meteor}

    armors_available = [mage_plate, archon_plate, heavy_plate]

    print('Przemierzasz świat aby ratować wioski i zabijać potwory, które je nękają...\n')

    hero.get_basic_weapon()

    def shop():

        while True:
            compare_weapons = [i for i in weapons_available if i not in hero.weapon]
            compare_spells = {k: v for (k, v) in spells_available.items() if k not in hero.spells}
            compare_armors = [i for i in armors_available if i not in hero.armor]

            display_items = int(input('Witaj w sklepie!\n'
                                      'Tutaj możesz uzbroić się w zbroję, tarczę, broń lub kupić czary.\n'
                                      'Aby wyświetlić dostępne przedmioty wpisz odpowiednio:\n'
                                      '1 - bronie\n'
                                      '2 - czary\n'
                                      '3 - zbroje\n'
                                      '0 - wyjście\n'))
            print('-' * 20 + '\n')

            if display_items == 0:
                break
            elif display_items == 1:
                display_items = weapons_available
                for compare in compare_weapons:
                    print(compare.description())
            elif display_items == 2:
                display_items = spells_available
                for compare in compare_spells.values():
                    print(compare.description())
            elif display_items == 3:
                display_items = armors_available
                for compare in compare_armors:
                    print(compare.description())
            else:
                print('Nie ma takiego numeru.')

            while True:
                item_name = input('\nWpisz nazwę przedmiotu, który chcesz kupić '
                                  'lub naciśnij ENTER, aby wrócić do sklepu: ').lower()
                print('-' * 20 + '\n')
                if item_name == '':
                    break
                if display_items == spells_available:
                    if not hero.has_spell_potion(display_items, item_name):
                        if hero.buy_spell_potion(display_items, item_name):
                            break
                if not hero.has_weapon_armor(display_items, item_name):
                    if hero.buy_weapon_armor(display_items, item_name):
                        break
                print('Masz juź ten przedmiot lub nie ma takiego przedmiotu.\n')


    def fight():

        if hero.lvl <= 5:
            monster = Rat('szczur')
        elif 6 <= hero.lvl <= 15:
            monster = Ogre('ogr')
        else:
            monster = Troll('troll')

        print(f'Wędrując przez krainę natknąłeś się na ogromnego, brzydkiego {monster}a')

        while monster.health > 0:
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
                if hero.has_armor():
                    hero.armor_defence(monster)
                    monster.attack(hero)
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
                    hero.spend_points()
            if hero.health <= 0:
                hero.die()
                break


    while hero.health > 0:

        fight()

        print(f'Posiadasz {hero.gold} sztuk złota.\n')
        go_to_shop = input('Wpisz "sklep" aby przejsc do sklepu.\n')
        print('-' * 20 + '\n')
        if go_to_shop == 'sklep':
            shop()
        continue
