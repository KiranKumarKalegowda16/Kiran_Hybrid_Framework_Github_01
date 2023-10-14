import random
import string

class Generic_Utilities:

    """ random_generator() function generates the random characters which can used where ever random values required """

    @staticmethod
    def random_genrator(size=8, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for x in range(size))
