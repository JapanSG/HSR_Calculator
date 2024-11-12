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
        self.order = [[char, 10000, 10000/char.get_spd()] for char in characters]
        self.order.sort(key = lambda x : x[2])

    def update(self) -> None:
        '''Update turn order'''
        av_passed = self.order[0][2]
        if not av_passed:
            print("Did Action")
            self.do_action()
            return
        for i in range(len(self.order)):
            item = self.order[i]
            spd = item[0].get_spd()
            self.order[i] = [item[0], item[1]-spd*av_passed, item[2]-av_passed]

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
        item = self.order.pop(0)
        new = [item[0], 10000, 10000/item[0].get_spd()]
        self._insert(new)
        
    def _insert(self, item: list):
        '''insert item at correct av'''
        for i in range(len(self.order)):
            if self.order[i][2] > item[2]:
                self.order.insert(i, item)
                return
        self.order.append(item)

def main():
    '''Driver Code'''
    ally1 = character.Ally("ally1",(100,300,100))
    ally2 = character.Ally("ally2",(100,300,120))
    ally3 = character.Ally("ally3",(100,300,140))
    enemy1 = character.Enemy("enemy1",(100,300,80))
    enemy2 = character.Enemy("enemy2",(100,300,95))
    enemy3 = character.Enemy("enemy2",(100,300,100))
    order = TurnManager(ally1,ally2,ally3,enemy1,enemy2,enemy3)
    order.print_order()
    order.update()
    print("-"*50)
    order.print_order()
    order.update()
    print("-"*50)
    order.print_order()
    order.update()
    print("-"*50)
    order.print_order()
    order.update()
    print("-"*50)
    order.print_order()

if __name__ == "__main__":
    main()
