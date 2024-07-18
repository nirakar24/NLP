import string


def tokenize_text(text):
    for char in string.punctuation:
        text = text.replace(char, " ")

    tokens = text.split()
    return tokens

# Using NLTK library

# import nltk
# from nltk.tokenize import sent_tokenize, word_tokenize
# nltk.download('punkt')

# def tokenize_text(text):
#     tokens = sent_tokenize(text)
#     return tokens

# text = "Hey, I hope you are doing good. Can I ask for some help?"
# print(tokenize_text(text))


