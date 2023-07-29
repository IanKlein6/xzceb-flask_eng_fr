import unittest

from translator import english_to_french, french_to_english


class TestEn2Fr(unittest.TestCase):
    """ Test 'Hello' Translation En/F """
    def test_1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')  

        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

    """ Test 'Bed' Translation En/F """
    def test_2(self):
        self.assertEqual(english_to_french('bed'), 'lit')
        self.assertNotEqual(english_to_french('bed'), 'bed')

        self.assertEqual(french_to_english('lit'), 'bed')
        self.assertNotEqual(french_to_english('lit'), 'lit')

    """ Test 'Kitchen' Translation En/F """
    def test_3(self):
        self.assertEqual(english_to_french('kitchen'), 'Bếp')
        self.assertNotEqual(english_to_french('kitchen'), 'kitchen')

        self.assertEqual(french_to_english('Bếp'), 'kitchen')
        self.assertNotEqual(french_to_english('Bếp'), 'Bếp')

if __name__ == '__main__':
    unittest.main()
