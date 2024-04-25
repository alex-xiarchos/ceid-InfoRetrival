from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import tools


def preprocess_collection():
    doc_tuples_list = tools.get_docs()

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    stripped_docs = []

    for doc_tuple in doc_tuples_list:
        stripped_doc = [stemmer.stem(word.lower()) for word in doc_tuple[1] if word.lower() not in stop_words]
        stripped_doc_tuple = (doc_tuple[0], stripped_doc)  # (DocID, <stripped_doc>)
        stripped_docs.append(stripped_doc_tuple)
 
    return stripped_docs


def preprocess_queries():
    queries = tools.get_queries()

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    stripped_queries = []

    for query in queries:
        stripped_query = [stemmer.stem(word.lower()) for word in query.split() if word.lower() not in stop_words]
        stripped_queries.append(stripped_query)


    return stripped_queries