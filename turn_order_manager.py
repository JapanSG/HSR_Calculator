"""turn_order_manager"""

import skillpoint as sk
import ally_enemy_base
import ally as a
import enemy as e
import math as m


# TODO
# list of things to fix
# everyting is broken since structuring inheritance in the Character class and it's subclasses
# - do_action function
# - remove_dead function
class TurnManager:
    """
    TurnManager class
    Manages characters turn order
    and action values
    """

    def __init__(
        self, sp: sk.SkillPoint, *characters: ally_enemy_base.Character
    ) -> None:
        """
        Constructor
        self.order values = [character.Character, AG left, Current AV]
        """
        self.sp = sp
        self.running = True
        self.allies = [char for char in characters if isinstance(char, a.Ally)]
        self.enemies = [char for char in characters if isinstance(char, e.Enemy)]
        self.order = [
            [char, 10000, m.ceil(10000 / char.total_spd)] for char in characters
        ]  # item = [Character, AG left, current AV]
        self.order.sort(key=lambda item: item[2])

    def update(self) -> None:
        """Update turn order"""
        av_passed = self.order[0][2]
        if not av_passed:
            item = self.order.pop(0)
            self.do_action(item)
            new = [item[0], 10000, m.ceil(10000 / item[0].total_spd)]
            self.__insert(new)
            return
        for i in range(len(self.order)):
            item = self.order[i]
            total_spd = item[0].total_spd
            ag = max(item[1] - total_spd * av_passed, 0)
            av = max(item[2] - av_passed, 0)
            self.order[i] = [item[0], ag, av]

    def print_order(self, curr_ally_name) -> None:
        """Print Order"""
        print(f"{curr_ally_name:<20s}| Doing action")
        for item in self.order:
            print(f"{item[0].name:<20s}| {item[2]} AV")

    def __str__(self) -> str:
        """String"""
        lis = [[item[0].name, item[2], item[1]] for item in self.order]
        return f"{lis}"

    def do_action(self, item) -> None:
        """Do action when av == 0 and reset av"""
        if isinstance(item[0], ally_enemy_base.Ally):
            self.input_action(item[0])
        else:
            print("Enemy took turn")
        return print("Pass")

    def input_action(self, ally: ally_enemy_base.Ally):
        finished = False
        print(f"It's {ally.name} turn")
        while not finished:
            command = input("Please input command -> ")
            if command == "q":
                print("You have quit the program")
                self.running = False
                finished = True
            elif command == "help":
                print("List of Commands: `basic`, `skill`, `ult`")
            elif command == "order":
                self.print_order(ally.name)
            elif command == "hp":
                for enemy in self.enemies:
                    print(enemy.curr_hp)
            elif command == "va":
                print(*self.allies)
            elif command == "ve":
                print(*self.enemies)
            elif command == "sp":
                print(self.sp)
            else:
                finished = ally.input_action(command, self.enemies, self.sp)

    def __insert(self, item: list) -> None:
        """insert item at correct av"""
        for i in range(len(self.order)):
            if self.order[i][2] > item[2]:
                self.order.insert(i, item)
                return
        self.order.append(item)

    # FIXME
    def remove_dead(self) -> None:
        """remove character that have less than  0 hp"""
        dead_allies = []
        for i in range(len(self.allies)):
            if self.allies[i].curr_hp <= 0:
                dead_allies.append(i)
        for i in dead_allies:
            self.allies.pop(i)

        dead_enemies = []
        for i in range(len(self.enemies)):
            if self.enemies[i].curr_hp <= 0:
                dead_enemies.append(i)
        for i in dead_enemies:
            self.enemies.pop(i)

    def loop(self) -> None:
        """Main loop"""
        while True:
            if not self.running:
                break
            self.remove_dead()
            if not self.enemies:
                print("Victory")
                break
            if not self.allies:
                print("Defeat")
                break
            self.update()
        print("end")


def main():
    """Driver Code"""


if __name__ == "__main__":
    main()
