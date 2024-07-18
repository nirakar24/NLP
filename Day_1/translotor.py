from googletrans import Translator

def translation_tokens(tokens, des_language):
    transalator = Translator()
    translated_tokens = [transalator.translate(token, src = "en", dest= des_language).text for token in tokens]
    return translated_tokens

def translation_text(text, des_language):
    transalator = Translator()
    translated_text = transalator.translate(text, src = "en", dest= des_language).text
    return translated_text