import unittest

from translator import englishToFrench, frenchToEnglish


class TestEn2Fr(unittest.TestCase):
    #Test 'Hello' Translation En/F
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')  

        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')

    #Test 'Bed' Translation En/F
    def test2(self):
        self.assertEqual(englishToFrench('bed'), 'lit')
        self.assertNotEqual(englishToFrench('bed'), 'bed')

        self.assertEqual(frenchToEnglish('lit'), 'bed')
        self.assertNotEqual(frenchToEnglish('lit'), 'lit')
    
    def test3(self):
        self.assertEqual(englishToFrench('kitchen'), 'Bếp')
        self.assertNotEqual(englishToFrench('kitchen'), 'kitchen')

        self.assertEqual(frenchToEnglish('Bếp'), 'kitchen')
        self.assertNotEqual(frenchToEnglish('Bếp'), 'Bếp')

if __name__ == '__main__':
    unittest.main()

