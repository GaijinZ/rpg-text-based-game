from hero import Hero
from enemy import Monster
from shop import monster_info, items_to_view, purchase_items
from effects import effect_to_make


def run_game():

    monsters_killed = 0

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
                    monster_info()

                if start_shop == '1':
                    items_to_view()

                    purchase_items(hero)

        print(f'Posiadasz {hero.gold} sztuk złota.\n')
        go_to_shop = input('Wpisz "sklep" aby przejsc do sklepu '
                           'lub naciśnj ENTER aby przejśc dalej.\n').lower()
        print('-' * 20 + '\n')
        if go_to_shop == 'sklep':
            shop()

        monster = Monster().monster_type(hero.lvl)

        if monsters_killed == 8:
            monster.boss()
        else:
            print(f'Wędrując przez krainę natknąłeś się na ogromnego, brzydkiego {monster.name}a, \n'
                  f'Odpornośc na: {monster.immune}\n')

        if hero.armor:
            hero.add_armor_bonus()

        hero.health = hero.max_health
        hero.mana = hero.max_mana

        while monster.current_health > 0:

            hero.check_for_effect()

            print(f'Masz {hero.health} punktów życia i {hero.mana} punktów many.\n')
            print(f'Potwór posiada {monster.current_health} punktów życia.\n')

            while True:

                attack = int(input('Wybierz 1 jeżeli chcesz zaatakować mieczem.\n'
                                   'Wybierz 2 jeżeli chesz zaatakować czarem.\n'
                                   'Wybierz 3 jeżeli chcesz użyć mikstury.\n'))
                if attack < 4:
                    break
            print('-' * 20 + '\n')

            if attack == 1:
                hero.attack_with_sword(monster)
            elif attack == 2:
                print('Twoje czary to:\n')
                hero.show_skills()
                choose_spell = input('Wpisz nazwę czaru, którym chcesz zaatakować: ')
                print('-' * 20 + '\n')
                if hero.has_spell(choose_spell):
                    spell = hero.get_spell_class()
                    if not monster.has_immune(spell, hero):
                        spell.additional_effect(monster)
                        hero.attack_with_spell(spell, monster)
                    else:
                        print(f'{monster.name} posiada niewrażliwość na {monster.immune}\n')
            elif attack == 3:
                hero.show_potions()
                choose_potion = input('\nWybierz miksturę, którą chcesz użyć: ')
                if choose_potion == '':
                    continue
                print('-' * 20 + '\n')
                if hero.has_potion(choose_potion):
                    hero.effects.append(effect_to_make[choose_potion])
                    hero.use_potion_effect(monster)
                    del hero.potions[choose_potion]
            if monster.current_health > 0:
                if monster.frozen > 0:
                    print('Potwór zamrożony, nie odnosisz obrażeń.\n')
                    monster.frozen -= 1
                else:
                    monster.attack()
                    monster.hit(hero)
            else:
                monster.die()
                monsters_killed += 1
                monster.get_exp_and_gold(hero)
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

    print('Przemierzasz świat aby ratować wioski i zabijać potwory, które je nękają...\n')

    run_game()
