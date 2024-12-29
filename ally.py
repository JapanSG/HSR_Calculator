'''ally'''
import random
import time
from ally_enemy_base import Ally
import enemy as e
import damage
import skillpoint
import event

class DestructionTrailblazer(Ally):
    '''DestructionTrailblazer'''
    def __init__(self, level:int, observer : event.EventManager, **kwargs) -> None:
        name = "Trailblazer"
        base_stats = (1203,620,460,100)
        super().__init__(name, level,'physical', base_stats, observer, max_energy =  120, **kwargs)

    def basic(self, target: e.Enemy) -> None:
        '''basic attack'''
        dmg = damage.Damage(
            element = 'physical',
            mult = 1,
            hits = [1],
            char = self,
            target = target,
            observer = self.observer,
            basic = True
        )
        dmg.dmg_formula_ally()
        self.gain_energy(20)

    def skill(self, left_target: e.Enemy, mid_target : e.Enemy, right_target : e.Enemy) -> None:
        '''skill'''
        #dmg for left target
        if left_target:
            dmg1 = damage.Damage(
                element = 'physical',
                mult = 1.25,
                hits = [1],
                char = self,
                target = left_target,
                observer = self.observer,
                skill = True
            )
            dmg1.dmg_formula_ally()

        #dmg for mid target
        dmg2 = damage.Damage(
            element = 'physical',
            mult = 1.25,
            hits = [1],
            char = self,
            target = mid_target,
            observer = self.observer,
            skill = True)
        dmg2.dmg_formula_ally()

        #dmg for right target
        if right_target:
            dmg3 = damage.Damage(
            element = 'physical',
            mult = 1.25,
            hits = [1],
            char = self,
            target = right_target,
            observer = self.observer,
            skill = True
        )
            dmg3.dmg_formula_ally()

        #gain energy
        self.gain_energy(30)


    def ultimate(self, left_target: e.Enemy, mid_target : e.Enemy, right_target : e.Enemy) -> None:
        '''ultimate'''
        choose = input("Choose mode (1 = single, 2 = double) -> ")
        #If choose 1st mode
        if choose == "1":

            #Damage instance
            dmg = damage.Damage(
                element = 'physical',
                mult = 4.5,
                hits = [1],
                char = self,
                target = mid_target,
                observer = self.observer,
                ult = True
            )

            #Calculate dmg
            dmg.dmg_formula_ally()


        #If choose 2nd mode
        else:

            #1st damage instance
            dmg1 = damage.Damage(
                element = 'physical',
                mult = 1.62,
                hits = [1],
                char = self,
                target = left_target,
                observer = self.observer,
                ult = True
            )

            #Calculate 1st damage instance
            dmg1.dmg_formula_ally()

            #2nd damage instance
            dmg2 = damage.Damage(
                element = 'physical',
                mult = 2.7,
                hits = [1],
                char = self,
                target = mid_target,
                observer = self.observer,
                ult = True
            )

            #Calculate 1nd damage instance
            dmg2.dmg_formula_ally()

            #3rd damage instance
            dmg3 = damage.Damage(
                element = 'physical',
                mult = 1.62,
                hits = [1],
                char = self,
                target = right_target,
                observer = self.observer,
                ult = True
            )

            #Calculate 3rd damage instance
            dmg3.dmg_formula_ally()

        #gain energy
        self.gain_energy(5)

    def input_action(self, command : str, enemies : list, sp : skillpoint.SkillPoint):
        '''input function'''
        if command == 'basic':
            sp.use(1)
            target_index = int(input("Please input which enemy -> "))
            print(f"{enemies[target_index]} selected")
            time.sleep(0.3)
            self.basic(enemies[target_index])
        elif command == 'skill':
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
            if target_index < len(enemies)-1:
                right_target = enemies[target_index + 1]

            mid_target = enemies[target_index]
            self.skill(left_target, mid_target, right_target)
        elif command == 'ult':
            if self.curr_energy < self.stats['max_energy']:
                print('Not enough energy to use ultimate')
                return False
            self.use_energy(self.stats["max_energy"])
            target_index = int(input("Please input which enemy -> "))
            print(f"{enemies[target_index]} selected")
            time.sleep(0.3)
            left_target = None
            if target_index:
                left_target = enemies[target_index - 1]

            right_target = None
            if target_index < len(enemies)-1:
                right_target = enemies[target_index + 1]

            mid_target = enemies[target_index]

            self.ultimate(left_target, mid_target, right_target)
        else:
            print("Invalid Command")
            return False
        return True

def __main():
    '''Driver Code'''
    # sp = skillpoint.SkillPoint()
    # observer = event.EventManager()
    # mc = DestructionTrailblazer(80,observer, taunt = 125.0)
    # enemy = e.Enemy("enemy",80,(2000,500,500,80),observer)
    # observer.attach(enemy)
    # print(enemy.curr_hp)
    # mc.basic(enemy,sp)

if __name__ == "__main__":
    __main()
