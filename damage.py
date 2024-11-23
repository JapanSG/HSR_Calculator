'''damage'''
import custom_exception as ex
ELEMENTS = ["fire", "ice", "physical", "lightning", "wind", "quantum", "imaginary"]
class Damage:
    '''Damage class'''

    def __init__(self,element : str, base : float, mult : float, hits : tuple, **kwargs):
        #ratio between hit ex. (1,1,3) = first hit deals 1/5, second deals 1/5, third deals 3/5
        '''Constructor'''
        self.type = {
            "basic" : kwargs.get('basic', False),
            "skill" : kwargs.get('skill',False),
            "ult" : kwargs.get('ult',False),
            "fua" : kwargs.get('fua',False),
            "dot" : kwargs.get('dot',False),
            "break" : kwargs.get('break',False),
            "additional" : kwargs.get('additional',False)
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
    def dmg_formula(self):
        base_dmg = self.mult * self.base 
        
def __test():
    '''Driver Code'''
    a = Damage('fire', 40, basic = True)
    print(a)

if __name__ == "__main__":
    __test()
