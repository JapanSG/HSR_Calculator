'''custom_exception'''
class NoSuchElement(Exception):
    '''Exception class for custom error scenarios.'''

    def __init__(self, element: str) -> None:
        '''Constructor'''
        super().__init__()
        self.element = element

    def __str__(self):
        '''str method'''
        return f"There is no element '{self.element}' in ELEMENTS"

if __name__ == "__main__":
    raise NoSuchElement('water')
