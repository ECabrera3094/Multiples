import unittest

class Multiples(unittest.TestCase):

    def test_multiples(self):

        number = Check()
        n = number.check_multiples()
        for i in n:
            print(i)

    

class Check():

    def check_multiples(self):
        
        for x in range(1, 101):
            if (x % 3 == 0) and (x % 5 == 0):
                yield "Linianos"
            elif x % 3 == 0:
                yield "Linio"
            elif x % 5 == 0:
                yield "IT"
            else:
                yield x

if __name__ == '__main__':
    unittest.main()