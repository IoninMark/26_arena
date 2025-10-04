from random import choice, choices, randint, sample

from constants import *


class Thing:
    """Класс шмотки."""

    def __init__(
            self,
            name: str,
            protection: int,
            attack: int,
            hp: int,
        ) -> None:
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp


class Person:
    """Базовый класс персонажа."""

    def __init__(
            self,
            hp: int,
            base_attack: int,
            base_protection: int,
            name: str,
        ) -> None:
        self.hp = hp
        self.attack = base_attack
        self.protection = base_protection
        self.name = name
    
    def set_things(self, things: list[Thing] | tuple[Thing]) -> None:
        """Метод добавления шмоток персонажу."""
        self.things = things
        for thing in things:
            self.hp += thing.hp
            self.attack += thing.attack
            self.protection += thing.protection
    
    def get_damage(self, damage: int) -> None:
        """Метод получения урона персонажем."""
        self.hp -= int(damage * (1 - self.protection / 100))


class Paladin(Person):
    """Класс паладина."""

    def __init__(self, hp: int, base_attack: int, base_protection: int, name: str) -> None:
        super().__init__(hp, base_attack, base_protection, name)
        self.hp *= 2
        self.protection *= 2
    

class Warrior(Person):
    """Класс воина."""
    
    def __init__(self, hp: int, base_attack: int, base_protection: int, name: str) -> None:
        super().__init__(hp, base_attack, base_protection, name)
        self.attack *= 2


def create_things(count=THINGS_COUNT) -> list[Thing]:
    """Ф-ия создания вещей."""
    things = []
    for _ in range(count):
        name = choice(THING_NAMES)
        THING_NAMES.remove(name)
        hp = randint(0, 100)
        protection = randint(0, 10)
        attack = randint(0, 50)
        things.append(Thing(
            name=name,
            protection=protection,
            attack=attack,
            hp=hp
        ))
    return things


def create_players(things: list[Thing], count=PLAYERS_COUNT) -> list[Person]:
    """Ф-ия создания игроков."""
    players = []
    for _ in range(count):
        name = choice(PLAYERS_NAMES)
        PLAYERS_NAMES.remove(name)
        things_count = randint(0, 4)
        player_things = choices(things, k=things_count)
        character_type = choice([Paladin, Warrior])
        player = character_type(
            hp=BASE_HP,
            base_attack=BASE_ATTACK,
            base_protection=BASE_PROTECTION,
            name=name
        )
        player.set_things(player_things)
        players.append(player)
    return players


def main():
    things = create_things()
    players = create_players(things=things)
    while len(players) > 1:
        battle_members = sample(players, k=2)
        defending_player, attack_player = battle_members
        print(f'{attack_player.name} наносит удар по {defending_player.name} на {attack_player.attack} урона.')
        defending_player.get_damage(attack_player.attack)
        if defending_player.hp <= 0:
            players.remove(defending_player)
            print(f'{defending_player.name} выбывает!')
    print(f'Победил {players[0].name}!!!')


if __name__ == '__main__':
    main()