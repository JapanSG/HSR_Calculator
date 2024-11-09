'''damage'''
import custom_exception as ex
ELEMENTS = ["fire", "ice", "physical", "lightning", "wind", "quantum", "imaginary"]
class Damage:
    '''Damage class'''

    def __init__(
        self,
        element : str,
        mult : int,
        basic: bool = False,
        skill: bool = False,
        ult: bool = False,
        fua: bool = False,
        dot: bool = False,
        breaks : bool = False,
        additional : bool = False
    ):
        '''Constructor'''
        self.type = {
            "basic" : basic,
            "skill" : skill,
            "ult" : ult,
            "fua" : fua,
            "dot" : dot,
            "break" : breaks,
            "additional" : additional
        }
        if element not in ELEMENTS:
            raise ex.NoSuchElement(element)
        self.element = element
        self.mult = mult

    def __str__(self):
        '''str'''
        return f"Element : {self.element}\nMultiplyer : {self.mult}%\nType : {[dtype for dtype in self.type if self.type[dtype]]}"

def __test():
    '''Driver Code'''
    a = Damage('fire', 40, basic = True)
    print(a)

if __name__ == "__main__":
    __test()
