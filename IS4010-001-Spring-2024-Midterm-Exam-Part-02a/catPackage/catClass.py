#catClass.py

# 1. Complete the sayMeow method
# 2. Complete the getName method

class Cat:
    '''
    Cat Class
    This class models a pet cat's name and meow
    '''
    def __init__(self, name):
        '''
        @param: name - name of the Cat
        '''
        self.name = name
    
    def sayMeow(self):
        '''
        Print meow to the console
        '''
        print("meow")
    
    def getName(self):
        '''
        Get the name of the Cat object
        @return: The name of the Cat object
        '''
        return self.name
    