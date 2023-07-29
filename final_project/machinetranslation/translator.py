"""
Translator Module.

This module contains functions for translating text between English and French languages.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French.

    Args:
        english_text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English.

    Args:
        french_text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    print(english_text)
    return english_text
