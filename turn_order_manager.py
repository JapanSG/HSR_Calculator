'''turn_order_manager'''
import character
import ally as a
import enemy as e
import skillpoint as s
import math as m
# TODO
# list of things to fix
# everyting is broken since structuring inheritance in the Character class and it's subclasses
# - do_action function
# - remove_dead function
class TurnManager:
    '''
    TurnManager class
    Manages characters turn order
    and action values
    '''
    def __init__(self, *characters : character.Character) -> None:
        '''
        Constructor
        self.order values = [character.Character, AG left, Current AV]
        '''
        self.running = True
        self.allies = [char for char in characters if isinstance(char, a.Ally)]
        self.enemies = [char for char in characters if isinstance(char, e.Enemy)]
        self.order = [[char, 10000, m.ceil(10000/char.spd)] for char in characters]
        self.order.sort(key = lambda item : item[2])

    def update(self) -> None:
        '''Update turn order'''
        av_passed = self.order[0][2]
        if not av_passed:
            item = self.order.pop(0)
            self.do_action()
            new = [item[0], 10000, m.ceil(10000/item[0].spd)]
            self._insert(new)
            return
        for i in range(len(self.order)):
            item = self.order[i]
            spd = item[0].spd
            ag = max(item[1] - spd*av_passed, 0)
            av = max(item[2] - av_passed, 0)
            self.order[i] = [item[0], ag, av]

    def print_order(self) -> None:
        '''Print Order'''
        lis = [[item[0].name, item[2], item[1]] for item in self.order]
        for item in lis:
            print(*item, sep = "	")

    def __str__(self) -> str:
        '''String'''
        lis = [[item[0].name, item[2], item[1]] for item in self.order]
        return f"{lis}"

    def do_action(self) -> None:
        '''Do action when av == 0 and reset av'''
        #FIXME
        a = input()
        if a == "q":
            self.running = False
        return print("Pass")
        item = self.order.pop(0) # item = [Character, AG left, current AV]
        # if isinstance(item[0], character.Ally):
        #     print(*self.enemies)
        #     print(*self.allies)
        #     target = int(input("choose which enemy to attack"))
        #     item[0].basic(self.enemies[target-1])
        # else:
        #     print("Enemy took turn")
        new = [item[0], 10000, 10000/item[0].spd()]
        self._insert(new)
        
    def _insert(self, item: list) -> None:
        '''insert item at correct av'''
        for i in range(len(self.order)):
            if self.order[i][2] > item[2]:
                self.order.insert(i, item)
                return
        self.order.append(item)

    def input_action(ally:a.Ally, string:str) ->None:
        '''input'''

    # FIXME
    def remove_dead(self) -> None:
        '''remove character that have less than  0 hp'''
        dead_allies = []
        for i in range(len(self.allies)):
            if self.allies[i].hp <= 0:
                dead_allies.append(i)
        for i in dead_allies:
            self.allies.pop(i)

        dead_enemies = []
        for i in range(len(self.enemies)):
            if self.enemies[i].hp <= 0:
                dead_enemies.append(i)
        for i in dead_enemies:
            self.enemies.pop(i)

    def loop(self) -> None:
        '''Main loop'''
        i = 0
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
            self.print_order()
            print("-"*25,i,"-"*25)
            i += 1
        print("end")

def main():
    '''Driver Code'''
    ally1 = a.Ally("ally1",(100,1000,100,100))
    ally2 = a.Ally("ally2",(100,1000,100,120))
    ally3 = a.Ally("ally3",(100,1000,100,140))
    enemy1 = e.Enemy("enemy1",(100,1000,100,150))
    enemy2 = e.Enemy("enemy2",(100,1000,100,95))
    enemy3 = e.Enemy("enemy2",(100,1000,100,100))
    order = TurnManager(ally2,enemy1,ally1,ally3,enemy2,enemy3)
    order.loop()

if __name__ == "__main__":
    main()
