import unittest

def reverse(s):
    return 'olleh'                            # this function must return the reverse of string `s`
                                            # replace this code with your own code

class ReverseString(unittest.TestCase): 

    def test_reverse(self):
        input = 'hello'
        output = reverse(input)
        self.assertEqual('olleh', output)     # replace this code with your own code



if __name__ == '__main__':
    unittest.main()