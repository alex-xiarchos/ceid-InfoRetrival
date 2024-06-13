import math
import numpy as np
from numpy.linalg import norm


def idf1(N, n):
    return math.log(N / n)


def idf2(N, n):
    return math.log(N - n / n)


def get_value(item):
    return item[1]


def vsm(doc_collection, query, inverted_index, model_type):
    query_tfidfs = {}
    doc_tfidfs = {}
    for doc in doc_collection:
        doc_tfidfs[doc[0]] = []  # Αρχικοποίηση λεξικού tf-idf τιμών με άδειες λίστες για κάθε έγγραφο

    # Υπολογισμός TF όρων για το ερώτημα:
    query_tfs = {}
    for term in query:
        query_tfs[term] = query.count(term)

    # Υπολογισμός TF-IDF τιμών. Διατρέχουμε κάθε όρο από το ερώτημα...
    for term in query:
        docs_containing_term = set()

        # Αν ο όρος του ερωτήματος υπάρχει στο ανεστραμμένο ευρετήριο, υπολογίζουμε την IDF τιμή του.
        if term in inverted_index:
            if model_type == "1":
                idf = idf1(len(doc_collection), len(inverted_index[term]))
            elif model_type == "2":
                idf = idf2(len(doc_collection), len(inverted_index[term]))

            # και την TF-IDF τιμή, δηλαδή το ΒΑΡΟΣ ΟΡΟΥ ΕΡΩΤΗΜΑΤΟΣ
            if model_type == "1":
                query_tfidfs[term] = (0.5 + 0.5 * (query_tfs[term] / max(query_tfs.values()))) * idf
            elif model_type == "2":
                query_tfidfs[term] = idf

            # Υπολογισμός TF-IDF τιμών για τα έγγραφα:
            for item in inverted_index[term]:
                docs_containing_term.add(item[0])
                # το docs_containing_term περιέχει τα έγγραφα που περιέχουν τον συγκεκριμένο όρο.

            # διατρέχουμε τα έγγραφα του docs_containing_term...
            for doc in doc_collection:
                if doc[0] in docs_containing_term:
                    # έγγραφο βρέθηκε - υπολογίζουμε TF
                    for item in inverted_index[term]:
                        if item[0] == doc[0]:
                            doc_tf = item[1]
                            break
                    # υπολογισμός TFIDF
                    if model_type == "1":
                        doc_tfidfs[doc[0]].append(doc_tf * idf1(len(doc_collection), len(inverted_index[term])))
                    elif model_type == "2":
                        doc_tfidfs[doc[0]].append(0.5 + 0.5 * (query_tfs[term] / max(query_tfs.values())))
                else:
                    # δε βρέθηκε έγγραφο, 0 στο διάνυσμα
                    doc_tfidfs[doc[0]].append(0)

    similarity = {}
    for doc in doc_tfidfs:
        similarity[doc] = np.dot(list(query_tfidfs.values()), doc_tfidfs[doc]) / (
                    norm(list(query_tfidfs.values())) * norm(doc_tfidfs[doc]))

    # μετατροπή nan τιμών σε 0
    similarity = {k: 0 if np.isnan(v) else v for k, v in similarity.items()}
    sort_similarity = sorted(similarity.items(), key=get_value)

    return sort_similarity[-100:][::-1]


def run_vsm(doc_collection, queries, inverted_index):
    results1 = []
    results2 = []

    for query in queries:
        results1.append(vsm(doc_collection, query, inverted_index, "1"))
        results2.append(vsm(doc_collection, query, inverted_index, "2"))

    return results1, results2
# fdsfds