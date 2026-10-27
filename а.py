import time
import random

inventory = {
    "монета": 50,
}
inventory_damage = {}
gun_on_path = True
roll = random.random()
equipped_weapon = ""
player_hp = 70
player_max_hp = 100


def use_item(item_name, digit=1):
    global player_hp
    item_name = item_name.lower()

    if item_name not in inventory or inventory[item_name] <= 0:
        if item_name == "монета":
            print(f"Недостаточно монет! У вас есть 0 шт., а нужно {digit}.")
        else:
            print(f"У вас нет предмета: {item_name}!")
        return False

    if inventory[item_name] < digit:
        if item_name == "монета":
            print(f"Недостаточно монет! У вас есть {inventory[item_name]} шт., а нужно {digit}.")
        else:
            print(f"Недостаточно предметов! У вас есть {inventory[item_name]} шт., а нужно {digit}.")
        return False

    inventory[item_name] -= digit

    if item_name == "зелье лечения":
        player_hp += 30 * digit
        if player_hp > player_max_hp:
            player_hp = player_max_hp
        print(f"Вы восстановили здоровье! Текущее ХП: {player_hp}/{player_max_hp}")

    if inventory[item_name] == 0:
        if item_name == "монета":
            print("У вас закончились монеты!")
        else:
            del inventory[item_name]
            if item_name in inventory_damage:
                del inventory_damage[item_name]
        print(f"Вы использовали все предметы: {item_name}!")
    else:
        if item_name == "монета":
            print(f"Вы потратили {digit} шт. монет. Осталось: {inventory[item_name]}")
        elif item_name != "зелье лечения":
            print(f"Вы использовали {item_name} ({digit} шт.). Осталось: {inventory[item_name]}")

    return True


def equip_weapon():
    global equipped_weapon
    while True:
        has_weapon = False
        print("--- Какое оружие ты хочешь взять в руки? ---")
        for item in inventory:
            if item in inventory_damage and inventory[item] > 0:
                print(f"- {item.capitalize()} (Урон: {inventory_damage[item]})")
                has_weapon = True

        if not has_weapon:
            print("[В инвентаре нет доступного оружия]")
            return

        choice = input("Введи название оружия (или 'выход' для отмены): ").lower()
        if choice == "выход":
            break

        if choice in inventory and choice in inventory_damage and inventory[choice] > 0:
            print(f"Ты выбрал: {choice.capitalize()}.")
            confirm = input("Хочешь оставить это оружие? (да / нет): ").lower()
            if confirm == "да" or confirm == "y":
                equipped_weapon = choice
                print(f"Ты взял в руки: {equipped_weapon.capitalize()}!")
                time.sleep(2.5)
                break
            else:
                print("Выбор отменен, выбирай заново.")
        else:
            print("[Ошибка!] У тебя нет такого оружия или ты ввёл название неправильно. Попробуй еще раз:")


def add_item(item_name, digit=1):
    item_name = item_name.lower()
    if item_name in inventory:
        inventory[item_name] += digit
        print(f"Вы подобрали предмет: {item_name} ({digit} шт.)")
    else:
        inventory[item_name] = digit
        print(f"Вы подобрали новый предмет: {item_name} ({digit} шт.)")


def add_gun(item_name, damage, digit=1):
    item_name = item_name.lower()
    if item_name in inventory:
        inventory[item_name] += digit
    else:
        inventory[item_name] = digit
    inventory_damage[item_name] = damage
    print(f"Вы подобрали новое оружие: {item_name} ({digit} шт.) с уроном {damage}")


def show_inventory():
    print("=== ВАШ ИНВЕНТАРЬ ===")
    print(f"Здоровье: {player_hp}/{player_max_hp}")
    print("-" * 21)
    for item, count in inventory.items():
        print(f"• {item.capitalize()}: {count} шт.")


def combat(monster_name, monster_hp, monster_damage):
    global player_hp, equipped_weapon
    monster_max_hp = monster_hp
    print(f"На вас напал {monster_name} ({monster_hp}/{monster_max_hp} ХП)!")
    time.sleep(2.0)

    while monster_hp > 0 and player_hp > 0:
        print(f"--- БОЙ ---")
        print(f"Ваше ХП: {player_hp}/{player_max_hp}")
        print(f"ХП врага: {monster_hp}/{monster_max_hp}")
        print("1 - Атаковать оружием")
        print("2 - Выпить зелье лечения (+30 ХП)")

        battle_choice = input("Твой ход: ")
        if battle_choice == "1":
            if equipped_weapon and equipped_weapon in inventory_damage:
                damage = inventory_damage[equipped_weapon]
                print(f"Ты бьешь, используя {equipped_weapon.capitalize()}!")
            else:
                damage = 1
                print("Ты бьешь голыми кулаками!")
            monster_hp -= damage
            print(f"Нанесено {damage} урона!")
            time.sleep(1.5)
        elif battle_choice == "2":
            if not use_item("зелье лечения"):
                continue
            time.sleep(1.5)
        else:
            print("Wabby Wabbo! Ты замешкался!")
            time.sleep(1.5)

        if monster_hp <= 0:
            break

        print(f"--- ХОД ВРАГА ---")
        enemy_attack = random.randint(1, monster_damage)
        player_hp -= enemy_attack
        print(f"{monster_name} наносит тебе {enemy_attack} урона!")
        time.sleep(1.5)
        print("-" * 43)

    if player_hp > 0:
        print(f"Вы победили {monster_name}!")
        return True
    else:
        print(f"Вас вырубили... Вы очнулись на базе.")
        player_hp = 20
        time.sleep(2.5)
        return False

print("-" * 43)
print("--- Добро пожаловать в RPG Test 1 Game! ---")
print("-" * 43)

while True:
    print("\n1 - пойти исследовать лес(можно найти лут)")
    print("2 - посмотреть инвентарь")
    print("3 - пойти в лавку торговца")
    print("4 - пойти на базу")

    choice1 = input("Выберите действие (1-4): ")

    if choice1 == "1":
        if gun_on_path:
            if combat("Пчела", 5, 1):
                time.sleep(1)
                if roll < 0.15:
                    add_gun("дробовик", 12)
                elif roll < 0.35:
                    add_gun("пистолет", 8)
                else:
                    add_gun("ржавый кинжал", 4)
                add_item("монета", 25)
                gun_on_path = False
            time.sleep(2.5)
        else:
            print("Вы уже тут были и всё забрали...")
            time.sleep(2.5)

    elif choice1 == "2":
        show_inventory()
        time.sleep(2.5)

    elif choice1 == "3":
        while True:
            print("--- ЛАВКА ТОРГОВЦА ---")
            print("Старик косится на твой кошелек:")
            print("1 - Купить зелье лечения(+30 хп) (30 монет)")
            print("2 - Купить пистолет (60 монет)")
            print("3 - Уйти из лавки")

            shop_choice = input("Что выберешь? ")
            if shop_choice == "1":
                if use_item("монета", 30):
                    add_item("зелье лечения")
                time.sleep(2.5)
            elif shop_choice == "2":
                if use_item("монета", 60):
                    add_gun("пистолет", 8)
                time.sleep(2.5)
            elif shop_choice == "3":
                print("Вы попрощались с торговцем и ушли...")
                time.sleep(2.5)
                break
            else:
                print("Wabby Wabbo!")
                time.sleep(2.5)

    elif choice1 == "4":
        print("Вы решили вернуться на базу и передохнуть...")
        time.sleep(1.5)
        equip_weapon()
        time.sleep(2.5)
        break

while True:
    print("")