class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'A ponny', 'Elephant', 'Wild Cat', 'Human']


    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print(f'\t{member}')
