import unittest
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='en-GB', target= 'fr-FR').translate(englishText)
    print(frenchText)
    return frenchText


def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='fr-FR', target= 'en-GB').translate(frenchText)
    print(englishText)
    return englishText


