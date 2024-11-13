'''turn_order_manager'''
import character

class TurnManager:
    '''
    TurnManager class
    Manages characters turn order
    and action values
    '''
    def __init__(self, *characters : character.Character) -> None:
        '''Constructor'''
        self.allies = [ally for ally in characters if isinstance(ally, character.Ally)]
        self.enemies = [enemy for enemy in characters if isinstance(enemy, character.Enemy)]
        self.order = [[char, 10000, round(10000/char.get_spd(),2)] for char in characters]
        self.order.sort(key = lambda x : x[2])

    def update(self) -> None:
        '''Update turn order'''
        av_passed = self.order[0][2]
        if not av_passed:
            self.do_action()
            return
        for i in range(len(self.order)):
            item = self.order[i]
            spd = item[0].get_spd()
            self.order[i] = [item[0], round(item[1]-spd*av_passed, 2), round(item[2]-av_passed, 2) ]

    def print_order(self) ->None:
        '''Print Order'''
        lis = [[item[0].name, item[2], item[1]] for item in self.order]
        for item in lis:
            print(*item)

    def __str__(self) -> str:
        '''String'''
        lis = [[item[0].name, item[2], item[1]] for item in self.order]
        return f"{lis}"

    def do_action(self) -> None:
        '''Do action when av == 0 and reset av'''
        item = self.order.pop(0) # item = [Character, AG left, current AV]
        if isinstance(item[0], character.Ally):
            print(self.enemies)
            target = int(input("choose which enemy to attack"))
            item[0].basic(self.enemies[target-1])
        else:
            print("Enemy too turn")
        new = [item[0], 10000, 10000/item[0].get_spd()]
        self._insert(new)
        
    def _insert(self, item: list) -> None:
        '''insert item at correct av'''
        for i in range(len(self.order)):
            if self.order[i][2] > item[2]:
                self.order.insert(i, item)
                return
        self.order.append(item)

    def remove_dead(self) -> None:
        '''remove character that have less than  0 hp'''
        dead_allies = []
        for i in range(len(self.allies)):
            if self.allies[i].get_hp() <= 0:
                dead_allies.append(i)
        for i in dead_allies:
            self.allies.pop(i)

        dead_enemies = []
        for i in range(len(self.enemies)):
            if self.enemies[i].get_hp() <= 0:
                dead_enemies.append(i)
        for i in dead_enemies:
            self.enemies.pop(i)

    def loop(self) -> None:
        '''Main loop'''
        i = 0
        while True:
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
    ally1 = character.Ally("ally1",(100,300,100))
    ally2 = character.Ally("ally2",(100,300,120))
    ally3 = character.Ally("ally3",(100,300,140))
    enemy1 = character.Enemy("enemy1",(100,300,150))
    enemy2 = character.Enemy("enemy2",(100,300,95))
    enemy3 = character.Enemy("enemy2",(100,300,100))
    print(enemy1)
    order = TurnManager(ally2,enemy1,ally1,ally3,enemy2,enemy3)
    order.loop()

if __name__ == "__main__":
    main()
