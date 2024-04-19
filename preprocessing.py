from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import json
import tools


def preprocess_collection():
    docs_list = tools.get_docs()

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    stripped_docs = []

    for doc in docs_list:
        stripped_doc = [stemmer.stem(word.lower()) for word in doc if word.lower() not in stop_words]
        stripped_docs.append(stripped_doc)

    with open('stripped_docs.json', 'w') as f:
        json.dump(stripped_docs, f)