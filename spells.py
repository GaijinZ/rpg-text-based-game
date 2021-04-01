import random


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
                  'Maksymalne obrażenia zwiekszone o 10.')
            return self.max_dmg


class IceBolt(Spell):
    name = 'ice bolt'
    dmg_type = 'zimno'
    min_dmg = 6
    max_dmg = 15
    mana = 7
    gold_required = 10
    lvl_required = 3

    def additional_effect(self):
        effect = random.randrange(2)
        if effect == 1:
            print('\nSkuteczny atak, przeciwnik zamarza na jedna turę.')


class Blizzard(Spell):
    name = 'blizzard'
    dmg_type = 'zimno'
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
                  'Maksymalne obrażenia zwiekszone o 25.')
            return self.max_dmg


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
            self.min_dmg = self.max_dmg
            print(f'\nSkuteczny atak {self.name}. Zadajesz maksymalne obrażenia.')
            return self.min_dmg


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


fireball = Fireball()
ice_bolt = IceBolt()
blizzard = Blizzard()
holy_light = HealingSpell()
earthquake = Earthquake()
meteor = Meteor()

spells_available = {'fireball': fireball,
                    'ice bolt': ice_bolt,
                    'blizzard': blizzard,
                    'holy light': holy_light,
                    'earthquake': earthquake,
                    'meteor': meteor}
