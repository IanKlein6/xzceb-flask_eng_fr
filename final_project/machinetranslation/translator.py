from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source='en-GB', target= 'fr-FR')
    frenchText = translator.translate(englishText)
    return frenchText


def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator(source='fr-FR', target= 'en-GB')
    englishText = translator.translate(frenchText)
    return englishText

