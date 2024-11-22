'''damage'''
import custom_exception as ex
ELEMENTS = ["fire", "ice", "physical", "lightning", "wind", "quantum", "imaginary"]
class Damage:
    '''Damage class'''

    def __init__(
        self,
        element : str,
        base : float,
        mult : float,
        hits : tuple, #ratio between hit ex. (1,1,3) = first hit deals 1/5, second deals 1/5, third deals 3/5
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
        self.base = base
        self.mult = mult
        self.hits = hits

    def __str__(self):
        '''str'''
        return (
            f"Element : {self.element}\n"
            f"Multiplyer : {self.mult}%\n"
            f"Type : {[dtype[0] for dtype in self.type.items() if dtype[1]]}"
        )

def __test():
    '''Driver Code'''
    a = Damage('fire', 40, basic = True)
    print(a)

if __name__ == "__main__":
    __test()
