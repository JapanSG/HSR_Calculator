'''skillpoint'''
class SkillPoint:
    '''skillpoint class'''
    def __init__(self, maximum : int = 5, curr : int = 3) -> None:
        '''Constructor'''

        if curr > maximum:
            raise ValueError("curr can not be more than max")
        if curr < 0 or max < 0:
            raise ValueError("max and curr cannot be less than 0")

        self.max = maximum
        self.curr = curr
    
    def __str__(self) -> str:
        '''str'''
        return f"{self.max}"

    def __repr__(self) -> int:
        '''repr'''
        return self.max

    def use(self, num : int) -> None:
        '''manager skill point recovery and usage'''
        updated = self.curr + num
        try :
            if updated < 0:
                self.curr = 0
                raise ValueError
            elif updated > self.max:
                self.curr = self.max
            else:
                self.curr = updated
        except ValueError:
            print("Skill point can not be lower than 0")
