# Example of removing stopwords from a given text using list comprehension
text=["AI engineering requiresd strong foundation in mathematics, programming, and domain knowledge."]

stopwords=["is","in","the","and","a","an","of","to","for","on","with","that","this","as","by","at","from","it","be","are","was","were","has","have","had"]

cleaned_text=[word for word in text[0].split() if word.lower() not in stopwords]

print(cleaned_text)