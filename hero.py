from items import *


class Hero:
    max_health = 500
    health = max_health
    max_mana = 30
    mana = max_mana
    defence = 0
    base_weapon_dmg = 100
    base_spell_dmg = 0
    gold = 100
    exp = 0
    lvl = 4
    level_up = 250

    dmg_done = 0

    armor = []
    weapon = []
    spells = {}
    potions = {}
    attributes = {'strength': 0, 'intelligence': 0, 'stamina': 0}

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Jestem {self.name}, przybyłem by zabijać potwory i palić wiedźmy.\n')

    def get_basic_weapon(self):
        base_weapon = BaseWeapon()
        return self.weapon.append(base_weapon)

    def sword_attack(self):
        if self.mana >= self.max_mana:
            self.mana = self.max_mana
        self.mana += 5
        weapon_attack = self.weapon[0]
        weapon_dmg = random.randint(weapon_attack.min_dmg, weapon_attack.max_dmg)
        self.dmg_done = weapon_dmg + self.base_weapon_dmg
        return self.dmg_done

    def has_spell_potion(self, item_group, item_name):
        if item_group == spells_available:
            item_group = self.spells
        elif item_group == potions_available:
            item_group = self.potions
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
            elif item_group == potions_available:
                item_group = self.potions
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

    def spell_attack(self, spell_name):
        if spell_name.mana > self.mana:
            print('\nNie mie masz wystarczającej ilości many.\n')
            return False
        if spell_name == 'holy_light':
            self.mana -= spell_name.mana
            self.health = self.max_health
            print('Uzupełiasz życie.\n')
            return True
        self.mana -= spell_name.mana
        min_dmg = spell_name.min_dmg
        max_dmg = spell_name.max_dmg
        spell_dmg = random.randint(min_dmg, max_dmg)
        self.dmg_done += spell_dmg + self.base_spell_dmg
        return self.dmg_done

    def hit(self, monster):
        monster.health -= self.dmg_done

    def has_armor(self):
        return self.armor

    def armor_bonus(self):
        self.max_health += self.armor[0].health
        self.defence += self.armor[0].defence

    def use_potion(self, potion, monster):
        if potion == healing_potion:
            self.health = self.max_health
            print('Uzpupełnisaz życie.\n')
        if potion == mana_potion:
            self.mana = self.max_mana
            print('Uzpupełnisaz manę.\n')
        # if potion == reduced_mana_potion:
        # spell_name.mana /= 0.5
        # print('Redukujesz manę o połowę przy następnym użyciu czaru.\n')
        if potion == double_dmg_potion:
            self.dmg_done *= 2
            print(f'Zadajesz podwójne obrażenia przy następnym ataku.\n')
        if potion == ignore_immune:
            monster.immune = None
            self.dmg_done = self.weapon[0].max_dmg
        return potion

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
                  f' koszt many {value.mana} punktów many, typ obrażeń {value.dmg_type}.\n')

    def show_potions(self):
        if not self.potions:
            print('Nie posiadasz żadnych miksturek.')
            return False
        for value in self.potions.values():
            print(f'{value.name} - {value.action}')

    def die(self):
        print('Stracileś wszystkie punkty życia. Nie żyjesz.\n')

    def __str__(self):
        return self.name
