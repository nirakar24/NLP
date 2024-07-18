import tokenisation
import translotor
import filter_tokens

text = input("Enter text : ")
language = input("Translate to (English : en, Hindi : hi, Marathi : mr, Odia : or, Japanese : ja) : ")

english_stopwords = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
    'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 
    'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
    'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 
    'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 
    'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 
    'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 
    't', 'can', 'will', 'just', 'don', 'should', 'now'
}


tokens = tokenisation.tokenize_text(text)
print(f"Tokens : {tokens}")
filtered_tokens = filter_tokens.filter_(tokens, english_stopwords)
print(f"Filtered tokens : {filtered_tokens}")
translated_tokens = translotor.translation_tokens(filtered_tokens, language)
print(f"Translated tokens : {translated_tokens}")
translated_text = translotor.translation_text(text, language)
print(f"Translation : {translated_text}")