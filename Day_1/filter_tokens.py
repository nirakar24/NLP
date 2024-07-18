def filter_(tokens, stopwords, min_length=0):
    filtered_tokens = []

    for token in tokens:
        if token.lower() not in stopwords and len(token)>min_length:
            filtered_tokens.append(token)
    
    return filtered_tokens