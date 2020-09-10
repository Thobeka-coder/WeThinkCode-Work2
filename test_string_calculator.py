import unittest

def add(numbers): 
    if numbers == "":       # The parameter 'numbers' is a string, and the function returns an integer
        return 0  
    if numbers == 1:
        return int(numbers) 
    if numbers == 2:
        return int(numbers)
    if numbers == 8:
        return int(numbers)        # replace this with your code

class StringCalculatorTests(unittest.TestCase):
    def test_sum_of_an_empty_string_should_be_0(self):
        self.assertEqual(add(""), 0)       # Replace this with your test code

    def test_sum_of_single_digit_should_be_the_number(self):
        self.assertEqual(add("1"),1)       # Replace this with your test code

    def test_sum_of_multi_digit_should_be_the_number(self):
        self.assertEqual(add("15"), 15)       # Replace this with your test code

    def test_sum_of_two_numbers(self):
        self.assertEqual(add("3,5"), 8)       # Replace this with your test code

  #  def test_sum_of_several_numbers(self):
       # self.assertEqual('Test not implemented yet')       # Replace this with your test code


if __name__ == '__main__':
    unittest.main()
