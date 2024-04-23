import math
from sklearn.metrics.pairwise import cosine_similarity

def idf1(N, n):
    return math.log(N/n)


def vsm1(doc_collection, query, inverted_index):
    placeholder = []

    # Δημιουργείται ένα dictionary της μορφής {'term': tf_value}, όπου terms τα terms του query
    query_tfs = {}
    for term in query:
        query_tfs[term] = query.count(term)

    doc_tfidfs = {}

    # for doc in doc_collection:
    #     tf_idf_docs[doc[0]] = []


    # Στο query_tfidfs αποθηκεύεται τα συνολικά βάρη όρου ερωτήματος για κάθε term του query
    query_tfidfs = {}

    for term in query:
        if term in inverted_index:
            # υπολογισμός IDF τιμής για το συγκεκριμένο term
            print(f"term: {term} \t len(inverted_index[term]): {len(inverted_index[term])}")
            idf = idf1(len(doc_collection), len(inverted_index[term]))
            # υπολογισμός tf-idf τιμής για το συγκεκριμένο term (βάρος όρου ερωτήματος) και αποθήκευση
            query_tfidfs[term] = (0.5 + 0.5*(query_tfs[term] / max(query_tfs.values()))) * idf

            # Αφού υπάρχει και υπολογιστεί το query_tfidfs, διατρέχουμε όλα τα έγγραφα,
            # βρίσκουμε το tf του όρου ανά κείμενο, και υπολογίζουμε το συνολικό tfidf για το έγγραφο.

            for doc in doc_collection:
                for tuple_ in inverted_index[term]:
                    print(term, tuple_)
                    doc_tfidfs[(term, tuple_[0])].append(tuple_[1] * idf1(len(doc_collection), len(inverted_index[term])))
                    print(doc_tfidfs[(term, tuple[0])])


    print(query_tfidfs, end="\n\n")

    return placeholder


def run_vsm(doc_collection, queries, inverted_index):
    results = []

    for query in queries:
        print(query)
        results = vsm1(doc_collection, query, inverted_index)
        elements = [int(item[0]) for item in results]
        results.append(elements)

    return results


