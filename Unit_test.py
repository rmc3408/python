
# ------------------------------------------------------ #
#  Unit.PY (be tested) and Unit _test.py (standart)      #
# ------------------------------------------------------ #


''' this standart test to check IF first letter is Uppercase
in EVERy WORD. <--However, To do in ALL words
we should use TITLE() ''' 

import unittest  # testing built-in function
import Unit      # filename to be tested

# class + nameofyourChoice(inheritance testCase)
class TestCap(unittest.TestCase):

    # this function will compare two files.
    def test_one_word(self):
        text = 'python' # Standart
        result = Unit.cap_text(text) # to be test
        self.assertEqual(result,'Python') # compare

    def test_multiple_words(self):
        text = 'multi python'
        result = Unit.cap_text(text)
        self.assertEqual(result,'Multi Python')

    def test_with_apostrophes(self):
        text = "monty python's flying circus"
        result = Unit.cap_text(text)
        self.assertEqual(result, "Monty Python's Flying Circus")

if __name__ == "__main__":
    unittest.main