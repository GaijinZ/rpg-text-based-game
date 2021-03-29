from hero import *
from enemy import Rat, Ogre, Troll

print('\nWITAJ W GRZE ŚMIERTELNIKU\n')
name = input("Wpisz imię bohatera: ")
print('-' * 20 + '\n')

hero = Hero(name)
hero.say_hello()

hero.get_basic_weapon()

monsters_killed = 0

print('Przemierzasz świat aby ratować wioski i zabijać potwory, które je nękają...\n')


def run_game():
    print(spells_available.get('fireball').additional_effect())
    global monsters_killed

    while hero.health > 0:
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
                                          '4 - mikstury\n'
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
                elif display_items == 4:
                    display_items = potions_available
                    for display in potions_available.values():
                        print(display.description())
                else:
                    print('Nie ma takiego numeru.')

                while True:
                    item_name = input('\nWpisz nazwę przedmiotu, który chcesz kupić '
                                      'lub naciśnij ENTER, aby wrócić do sklepu: ').lower()
                    print('-' * 20 + '\n')
                    if item_name == '':
                        break
                    if display_items == spells_available or display_items == potions_available:
                        if not hero.has_spell_potion(display_items, item_name):
                            if hero.buy_spell_potion(display_items, item_name):
                                break
                    if not hero.has_weapon_armor(display_items, item_name):
                        if hero.buy_weapon_armor(display_items, item_name):
                            break
                    print('Masz juź ten przedmiot lub nie ma takiego przedmiotu.\n')

        print(f'Posiadasz {hero.gold} sztuk złota.\n')
        go_to_shop = input('Wpisz "sklep" aby przejsc do sklepu '
                           'lub naciśnj ENTER aby przejśc dalej.\n')
        print('-' * 20 + '\n')
        if go_to_shop == 'sklep':
            shop()

        if hero.lvl <= 5:
            monster = Rat('szczur')
        elif 6 <= hero.lvl <= 15:
            monster = Ogre('ogr')
        else:
            monster = Troll('troll')

        if hero.has_armor():
            hero.armor_bonus()

        if monsters_killed == 8:
            monster.max_health *= 2
            monster.min_dmg *= 2
            monster.max_dmg *= 2
            print(f'Trafiasz na zmutowany gatunek {monster.monster_name},który posiada zwiekszone życie i obrażenia.\n'
                  'Bądź ostrożny.\n')
            monsters_killed = 0
        else:
            print(f'Wędrując przez krainę natknąłeś się na ogromnego, brzydkiego {monster}a, \n'
                  f'Odpornośc na: {monster.immune}')

        hero.health = hero.max_health
        hero.mana = hero.max_mana

        while monster.health > 0:

            print(f'\nMasz {hero.health} punktów życia i {hero.mana} punktów many.\n')
            print(f'Potwór posiada {monster.health} punktów życia.\n')

            while True:
                attack = int(input('Wybierz 1 jezeli chcesz zaatakować mieczem.\n'
                                   'Wybierz 2 jeżeli chesz zaatakować czarem\n'
                                   'Wybierz 3 jeżeli chesz użyć mikstury.\n'))
                if attack < 4:
                    break
            print('-' * 20 + '\n')

            if attack == 1:
                hero.sword_attack()
                hero.hit(monster)
                print(f'Atakujesz wroga za pomocą miecza za {hero.dmg_done} punktów życia.\n')
            elif attack == 2:
                print('\nTwoje czary to:\n')
                hero.show_skills()
                choose_spell = input('\nWpisz nazwę czaru, którym chcesz zaatakować: ')
                print('-' * 20 + '\n')
                if hero.has_spell_potion(spells_available, choose_spell):
                    get_spell = hero.spells.get(choose_spell)
                    if not monster.has_immune(get_spell, hero):
                        if spells_available.get(choose_spell).addtional_effect():
                            print('dodatkowy efekt')
                        hero.spell_attack(get_spell)
                        hero.hit(monster)
                        print(f'Atakujesz wroga za pomocą {choose_spell} za {hero.dmg_done} punktów życia.\n')
                    else:
                        print(f'{monster.monster_name} posiada niewrażliwość na {monster.immune}\n')
            elif attack == 3:
                hero.show_potions()
                choose_potion = input('Wybierz miksturę, którą chcesz użyć: ')
                print('-' * 20 + '\n')
                if hero.has_spell_potion(potions_available, choose_potion):
                    get_potion = hero.potions.get(choose_potion)
                    hero.use_potion(get_potion, monster)
            if monster.health > 0:
                monster.attack()
                monster.hit(hero)
            else:
                monster.die()
                monsters_killed += 1
                print(monsters_killed)
                monster.get_exp_and_gold(hero)
                if hero.lvl_up():
                    print(f'Awansujesz na poziom {hero.lvl}\n')
                    print(f'Twoje życie i mana zwiekszją się. Teraz wynoszą: {hero.max_health} i {hero.max_mana}\n')
                    hero.spend_points()
            if hero.health <= 0:
                hero.die()
                break


if __name__ == '__main__':
    run_game()
