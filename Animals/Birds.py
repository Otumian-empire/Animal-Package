class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'An actual flying ponny', 'Duck']


    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print(f'\t{member}')


