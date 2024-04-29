import math
import numpy as np
from numpy.linalg import norm


def idf1(N, n):
    return math.log(N/n)

def idf2(N, n):
    return math.log(N - n/n)

def get_value(item):
    return item[1]


def vsm1(doc_collection, query, inverted_index):
    query_tfs = {}
    for term in query:
        query_tfs[term] = query.count(term)
    # print(f"Αρχικοποίηση query_tfs: {query_tfs}", end="\n\n")

    query_tfidfs = {}

    doc_tfidfs = {}
    for doc in doc_collection:
        doc_tfidfs[doc[0]] = []

    for term in query:
        docs_containing_term = set()

        # print(f"Για τον όρο {term}:")
        if term in inverted_index:
            # υπολογισμός IDF τιμής για το συγκεκριμένο term
            # print(f"\t> len(inverted_index[term]): {len(inverted_index[term])}")
            idf = idf1(len(doc_collection), len(inverted_index[term]))
            # print(f"\t> IDF για τον όρο {term}: {idf}")
            # υπολογισμός tf-idf τιμής για το συγκεκριμένο term (βάρος όρου ερωτήματος) και αποθήκευση
            query_tfidfs[term] = (0.5 + 0.5*(query_tfs[term] / max(query_tfs.values()))) * idf
            # print(f"\t> Άρα το βάρος όρου ερωτήματος είναι: {query_tfidfs[term]}", end="\n\n")

            for item in inverted_index[term]:
                docs_containing_term.add(item[0])

            for doc in doc_collection:
                if doc[0] in docs_containing_term:
                    for item in inverted_index[term]:
                        if item[0] == doc[0]:
                            doc_tf = item[1]
                            break
                    doc_tfidfs[doc[0]].append(doc_tf * idf1(len(doc_collection), len(inverted_index[term])))
                else:
                    doc_tfidfs[doc[0]].append(0)

    similarity = {}
    for doc in doc_tfidfs:
        similarity[doc] = np.dot(list(query_tfidfs.values()), doc_tfidfs[doc]) / (norm(list(query_tfidfs.values())) * norm(doc_tfidfs[doc]))

    # μετατροπή nan τιμών σε 0
    similarity = {k: 0 if np.isnan(v) else v for k, v in similarity.items()}
    sort_similarity = sorted(similarity.items(), key=get_value)

    return sort_similarity[-100:][::-1]


def vsm2(doc_collection, query, inverted_index):
    query_tfs = {}
    for term in query:
        query_tfs[term] = query.count(term)

    query_tfidfs = {}

    doc_tfidfs = {}
    for doc in doc_collection:
        doc_tfidfs[doc[0]] = []

    for term in query:
        docs_containing_term = set()

        if term in inverted_index:
            idf = idf2(len(doc_collection), len(inverted_index[term]))
            query_tfidfs[term] = idf

            for item in inverted_index[term]:
                docs_containing_term.add(item[0])

            for doc in doc_collection:
                if doc[0] in docs_containing_term:
                    for item in inverted_index[term]:
                        if item[0] == doc[0]:
                            doc_tf = item[1]
                            break
                    doc_tfidfs[doc[0]].append(0.5 + 0.5*(query_tfs[term] / max(query_tfs.values())))
                else:
                    doc_tfidfs[doc[0]].append(0)

    similarity = {}
    for doc in doc_tfidfs:
        # similarity[doc] = cosine_similarity(list(query_tfidfs.values()), doc_tfidfs[doc])
        similarity[doc] = np.dot(list(query_tfidfs.values()), doc_tfidfs[doc]) / (norm(list(query_tfidfs.values())) * norm(doc_tfidfs[doc]))

    # μετατροπή nan τιμών σε 0
    similarity = {k: 0 if np.isnan(v) else v for k, v in similarity.items()}
    sort_similarity = sorted(similarity.items(), key=get_value)

    return sort_similarity[-100:][::-1]


def run_vsm(doc_collection, queries, inverted_index):
    results = []

    for query in queries:
        print(query)
        results = vsm1(doc_collection, query, inverted_index)

    return results
