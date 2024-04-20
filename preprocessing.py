from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import json
import tools


def preprocess_collection():
    doc_tuples_list = tools.get_docs()

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    stripped_docs = []

    for doc_tuple in doc_tuples_list:
        stripped_doc = [stemmer.stem(word.lower()) for word in doc_tuple[1] if word.lower() not in stop_words]
        stripped_doc_tuple = (stripped_doc, doc_tuple[0])
        stripped_docs.append(stripped_doc_tuple)

    with open('stripped_docs_tuples.json', 'w') as f:
        json.dump(stripped_docs, f)


def preprocess_queries():
    queries = tools.get_queries()

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    stripped_queries = []

    for query in queries:
        stripped_query = [stemmer.stem(word.lower()) for word in query.split() if word.lower() not in stop_words]
        stripped_queries.append(stripped_query)

    with open('stripped_queries.json', 'w') as f:
        json.dump(stripped_queries, f)