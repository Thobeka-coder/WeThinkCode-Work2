import unittest

def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'  #hard code a value that makes the test pass
    if n % 5 == 0:
        return 'buzz'
    return str(n)

class TestFizzBuzz(unittest.TestCase):             
    def test_divisible_by_3_is_fizz(self):                       
        self.assertEqual(fizzbuzz(3), 'fizz')  

    def test_divisible_by_5_is_buzz(self):
        self.assertEqual(fizzbuzz(5), 'fizz') 

    def test_divisible_by_3_and_5_is_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

    def test_any_other_number_is_number(self):
        self.assertEqual(fizzbuzz(37), '37')

if __name__ == '__main__':
    unittest.main()
