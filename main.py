from hero import Hero
from enemy import Monster
from shop import items_to_buy


def run_game():
    global monsters_killed

    while hero.health > 0:
        def shop():

            while True:
                print('Witaj w sklepie!\n'
                      'Tutaj możesz uzbroić się w zbroję, tarczę, broń lub kupić czary.\n'
                      'Aby kupić przedmiot najpierw wpisz jego kategorię np. armors, później jego nazwę.'
                      'Aby wyjść naciśnij ENTER.')

                for key, value in items_to_buy.items():
                    print(f'\n{key}\n')
                    for items in value.values():
                        print(items.description())

                while True:
                    item_category = input('\nWpisz kategorię przedmiotu: ').lower()
                    item_name = input('\nWpisz nazwę przedmiotu, który chcesz kupić: ').lower()
                    print('-' * 20 + '\n')

                    if item_name == '':
                        return False
                    buy_item = items_to_buy.get(item_category).get(item_name)
                    if item_name != str(buy_item):
                        print('Nie ma takiego przedmiotu.\n')
                        break
                    if hero.has_gold_lvl_required(buy_item):
                        hero.buy_from_shop(buy_item)
                        del items_to_buy[item_category][item_name]
                        print(f'{item_name} został dodany do Twoich przedmiotów.\n')
                        break

        print(f'Posiadasz {hero.gold} sztuk złota.\n')
        go_to_shop = input('Wpisz "sklep" aby przejsc do sklepu '
                           'lub naciśnj ENTER aby przejśc dalej.\n').lower()
        print('-' * 20 + '\n')
        if go_to_shop == 'sklep':
            shop()

        monster = Monster()

        monster.monster_type(hero)
        if monsters_killed == 2:
            monster.boss()
        else:
            print(f'Wędrując przez krainę natknąłeś się na ogromnego, brzydkiego {monster.type.name}a, \n'
                  f'Odpornośc na: {monster.type.immune}\n')

        if hero.armor is not None:
            hero.add_armor_bonus()

        hero.health = hero.max_health
        hero.mana = hero.max_mana

        while monster.type.health > 0:

            print(f'Masz {hero.health} punktów życia i {hero.mana} punktów many.\n')
            print(f'Potwór posiada {monster.type.health} punktów życia.\n')

            while True:
                attack = int(input('Wybierz 1 jeżeli chcesz zaatakować mieczem.\n'
                                   'Wybierz 2 jeżeli chesz zaatakować czarem\n'
                                   'Wybierz 3 jeżeli chcesz użyć mikstury.\n'))
                if attack < 4:
                    break
            print('-' * 20 + '\n')

            if attack == 1:
                hero.sword_attack()
                hero.hit(monster.type)
                print(f'Atakujesz wroga za pomocą miecza za {hero.dmg_done} punktów życia.\n')
            elif attack == 2:
                print('Twoje czary to:\n')
                hero.show_skills()
                choose_spell = input('Wpisz nazwę czaru, którym chcesz zaatakować: ')
                print('-' * 20 + '\n')
                if hero.has_spell_potion(hero.spells, choose_spell):
                    get_spell = hero.get_spell_class()
                    if not monster.type.has_immune(get_spell, hero):
                        get_spell.additional_effect()
                        hero.spell_attack()
                        hero.hit(monster.type)
                        print(f'Atakujesz wroga za pomocą {choose_spell} za {hero.dmg_done} punktów życia.\n')
                    else:
                        print(f'{monster.type.name} posiada niewrażliwość na {monster.type.immune}\n')
            elif attack == 3:
                hero.show_potions()
                choose_potion = input('Wybierz miksturę, którą chcesz użyć: ')
                print('-' * 20 + '\n')
                if hero.has_spell_potion(hero.potions.values(), choose_potion):
                    get_potion = hero.potions.get(choose_potion)
                    hero.potion_used = hero.use_potion(get_potion, monster.type)
            if monster.type.health > 0:
                monster.type.attack()
                monster.type.hit(hero)
            else:
                monster.die()
                monsters_killed += 1
                monster.type.get_exp_and_gold(hero)
                if hero.lvl_up():
                    print(f'Awansujesz na poziom {hero.lvl}\n')
                    print(f'Twoje życie i mana zwiekszją się. Teraz wynoszą: {hero.max_health} i {hero.max_mana}\n')
                    hero.spend_points()
            if hero.health <= 0:
                hero.die()
                break


if __name__ == '__main__':
    print('\nWITAJ W GRZE ŚMIERTELNIKU\n')
    name = input("Wpisz imię bohatera: ")
    print('-' * 20 + '\n')

    hero = Hero(name)
    hero.say_hello()

    hero.get_basic_weapon()

    monsters_killed = 0

    print('Przemierzasz świat aby ratować wioski i zabijać potwory, które je nękają...\n')

    run_game()
