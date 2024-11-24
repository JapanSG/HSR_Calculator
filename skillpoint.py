'''skillpoint'''
class SkillPoint:
    '''skillpoint class'''
    def __init__(self, maximum : int = 5, curr : int = 3) -> None:
        '''Constructor'''

        if curr > maximum:
            raise ValueError("curr can not be more than max")
        if curr < 0 or maximum < 0:
            raise ValueError("max and curr cannot be less than 0")

        self.max = maximum
        self.curr = curr
    
    def __str__(self) -> str:
        '''str'''
        return f"{self.curr}"

    def __repr__(self) -> int:
        '''repr'''
        return self.curr

    def use(self, num : int) -> None:
        '''manager skill point recovery and usage'''
        updated = self.curr + num
        if updated < 0:
            self.curr = 0
        elif updated > self.max:
            self.curr = self.max
        else:
            self.curr = updated
