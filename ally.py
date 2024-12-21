"""ally"""

import random
import time
from ally_enemy_base import Ally
import enemy as e
import damage
import skillpoint
import event


class DamageListener:
    """X attacked Y resulting in Z damages"""

    def update(self, action: list):
        if action[0] == event.DamageEvent:
            print(
                f"[{action[1]} attacked {action[2]} resulting in {action[4]:.2f} damage]"
            )


class DestructionTrailblazer(Ally):
    """DestructionTrailblazer"""

    def __init__(self, level: int, observer: event.EventManager, **kwargs) -> None:
        name = "Trailblazer"
        base_stats = (1203, 620, 460, 100)
        super().__init__(
            name, level, "physical", base_stats, observer, max_energy=120, **kwargs
        )

    def basic(self, target: e.Enemy) -> None:
        """basic attack"""
        damage.Damage(
            "physical", 1, [1], self, target, self.observer, basic=True
        ).dmg_formula_ally()
        self.gain_energy(20)

    def skill(
        self, left_target: e.Enemy, mid_target: e.Enemy, right_target: e.Enemy
    ) -> None:
        """skill"""
        if left_target:
            damage.Damage(
                "physical", 1.25, [1], self, left_target, self.observer, skill=True
            ).dmg_formula_ally()
        damage.Damage(
            "physical", 1.25, [1], self, mid_target, self.observer, skill=True
        ).dmg_formula_ally()
        if right_target:
            damage.Damage(
                "physical", 1.25, [1], self, right_target, self.observer, skill=True
            ).dmg_formula_ally()
        self.gain_energy(30)

    def ultimate(
        self, left_target: e.Enemy, mid_target: e.Enemy, right_target: e.Enemy
    ) -> None:
        """ultimate"""
        choose = input("Choose mode (1 = single, 2 = blast) -> ")
        if choose == "1":
            damage.Damage(
                "physical", 4.5, [1], self, mid_target, self.observer, ult=True
            ).dmg_formula_ally()
        else:
            damage.Damage(
                "physical", 1.62, [1], self, left_target, self.observer, ult=True
            ).dmg_formula_ally()
            damage.Damage(
                "physical", 2.7, [1], self, mid_target, self.observer, ult=True
            ).dmg_formula_ally()
            damage.Damage(
                "physical", 1.62, [1], self, right_target, self.observer, ult=True
            ).dmg_formula_ally()
        self.gain_energy(5)

    def input_action(self, command: str, enemies: list, sp: skillpoint.SkillPoint):
        if command == "basic":
            sp.use(1)
            target_index = int(input("Please input which enemy -> "))
            print(f"{enemies[target_index]} selected")
            time.sleep(0.3)
            self.basic(enemies[target_index])
        elif command == "skill":
            if not sp.curr:
                print("Not enough skill point")
                return False
            sp.use(-1)
            target_index = int(input("Please input which enemy -> "))
            print(f"{enemies[target_index]} selected")
            time.sleep(0.3)
            left_target = None
            if target_index:
                left_target = enemies[target_index - 1]

            right_target = None
            if target_index < len(enemies) - 1:
                right_target = enemies[target_index + 1]

            mid_target = enemies[target_index]
            self.skill(left_target, mid_target, right_target)
        elif command == "ult":
            if self.curr_energy < self.stats["max_energy"]:
                print("Not enough energy to use ultimate")
                return False
            self.use_energy(self.stats["max_energy"])
            target_index = int(input("Please input which enemy -> "))
            print(f"{enemies[target_index]} selected and caused damage")
            # TODO Display damage numbers
            time.sleep(0.3)
            left_target = None
            if target_index:
                left_target = enemies[target_index - 1]

            right_target = None
            if target_index < len(enemies) - 1:
                right_target = enemies[target_index + 1]

            mid_target = enemies[target_index]

            self.ultimate(left_target, mid_target, right_target)
        else:
            print("Invalid Command")
            return False
        return True


def __main():
    """Driver Code"""
    # sp = skillpoint.SkillPoint()
    # observer = event.EventManager()
    # mc = DestructionTrailblazer(80,observer, taunt = 125.0)
    # enemy = e.Enemy("enemy",80,(2000,500,500,80),observer)
    # observer.attach(enemy)
    # print(enemy.curr_hp)
    # mc.basic(enemy,sp)


if __name__ == "__main__":
    __main()
