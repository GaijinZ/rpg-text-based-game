from hero import Hero
from enemy import Monster
from shop import items_to_buy, monsters


def run_game():
    global monsters_killed

    while hero.health > 0:
        def shop():

            while True:
                start_shop = input('Witaj w sklepie!\n'
                                   'Tutaj możesz uzbroić się w zbroję, tarczę, broń lub kupić czary.\n'
                                   'Aby kupić przedmiot najpierw wpisz jego kategorię np. armors, później jego nazwę.\n'
                                   'Wybierz 1 aby wyświetlić przedmioty do kupienia.\n'
                                   'Wybierz 0 aby wyświetlić bestiariusz.\n'
                                   'Aby wyjść naciśnij ENTER.\n')
                print('-' * 20 + '\n')
                if start_shop == '':
                    break

                if start_shop == '0':
                    for monster_info in monsters.values():
                        print(monster_info.bestiary())

                if start_shop == '1':
                    for key, value in items_to_buy.items():
                        print(f'\n{key}\n')
                        for items in value.values():
                            print(items.description())

                    while True:
                        spells_effects = input(
                            '\nAby dowiedzieć się więcej o dodatkowych efektach czarów wpisz "efekty",'
                            ' wciśnij ENTER aby przejśc dalej ').lower()

                        if spells_effects == 'efekty':
                            for i in items_to_buy.get('spells').values():
                                print(i.additional_effect_info)

                        item_category = input('\nWpisz kategorię przedmiotu: ').lower()
                        item_name = input('\nWpisz nazwę przedmiotu, który chcesz kupić: ').lower()
                        print('-' * 20 + '\n')

                        if item_name == '':
                            return False
                        buy_item = items_to_buy.get(item_category).get(item_name)
                        if item_name != str(buy_item):
                            print('\nNie ma takiego przedmiotu.\n')
                            break
                        if hero.has_gold_lvl_required(buy_item):
                            hero.buy_from_shop(buy_item)
                            if item_category != 'potions':
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
        if monsters_killed == 8:
            monster.boss()
        else:
            print(f'Wędrując przez krainę natknąłeś się na ogromnego, brzydkiego {monster.type.name}a, \n'
                  f'Odpornośc na: {monster.type.immune}\n')

        if hero.armor is not None:
            hero.add_armor_bonus()

        hero.health = hero.max_health
        hero.mana = hero.max_mana

        while monster.type.current_health > 0:

            print(f'Masz {hero.health} punktów życia i {hero.mana} punktów many.\n')
            print(f'Potwór posiada {monster.type.current_health} punktów życia.\n')

            while True:
                attack = int(input('Wybierz 1 jeżeli chcesz zaatakować mieczem.\n'
                                   'Wybierz 2 jeżeli chesz zaatakować czarem.\n'
                                   'Wybierz 3 jeżeli chcesz użyć mikstury.\n'))
                if attack < 4:
                    break
            print('-' * 20 + '\n')

            if attack == 1:
                hero.sword_attack()
                if hero.potion_choice is not None:
                    hero.potion_choice.use_potion(hero, monster.type)
                    hero.hit(monster.type)
                else:
                    hero.hit(monster.type)
            elif attack == 2:
                print('Twoje czary to:\n')
                hero.show_skills()
                choose_spell = input('Wpisz nazwę czaru, którym chcesz zaatakować: ')
                print('-' * 20 + '\n')
                if hero.has_spell(choose_spell):
                    spell = hero.get_spell_class()
                    if not monster.type.has_immune(spell, hero):
                        spell.additional_effect(monster.type)
                        hero.spell_attack(spell)
                        if hero.potion_choice is not None:
                            hero.potion_choice.use_potion()
                            hero.hit(monster.type)
                        else:
                            hero.hit(monster.type)
                    else:
                        print(f'{monster.type.name} posiada niewrażliwość na {monster.type.immune}\n')
            elif attack == 3:
                hero.show_potions()
                choose_potion = input('\nWybierz miksturę, którą chcesz użyć: ')
                print('-' * 20 + '\n')
                if hero.has_potion(choose_potion):
                    hero.use_potion(choose_potion)
            if monster.type.health > 0:
                if monster.type.frozen > 0:
                    print('Potwór zamrożony, nie odnosisz obrażeń.\n')
                    monster.type.frozen -= 1
                else:
                    monster.type.attack()
                    monster.type.hit(hero)
            else:
                monster.type.die()
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
