import math
from sklearn.metrics.pairwise import cosine_similarity

def idf1(N, n):
    return math.log(N/n)


def vsm1(doc_collection, query, inverted_index):
    placeholder = []

    query_tfs = {}
    for term in query:
        query_tfs[term] = query.count(term)
    print(f"Αρχικοποίηση query_tfs: {query_tfs}", end="\n\n")

    query_tfidfs = {}

    for term in query:
        docs_containing_term = set()
        doc_tfidfs = {}
        for doc in doc_collection:
            doc_tfidfs[doc[0]] = []

        print(f"Για τον όρο {term}:")
        if term in inverted_index:
            # υπολογισμός IDF τιμής για το συγκεκριμένο term
            print(f"\t> len(inverted_index[term]): {len(inverted_index[term])}")
            idf = idf1(len(doc_collection), len(inverted_index[term]))
            print(f"\t> IDF για τον όρο {term}: {idf}")
            # υπολογισμός tf-idf τιμής για το συγκεκριμένο term (βάρος όρου ερωτήματος) και αποθήκευση
            query_tfidfs[term] = (0.5 + 0.5*(query_tfs[term] / max(query_tfs.values()))) * idf
            print(f"\t> Άρα το βάρος όρου ερωτήματος είναι: {query_tfidfs[term]}", end="\n\n")

            print(f"\t Υπολογισμός βάρους εγγράφων:")
            for item in inverted_index[term]:
                docs_containing_term.add(item[0])

            for doc in doc_collection:
                if doc[0] in docs_containing_term:
                    for item in inverted_index[term]:
                        if item[0] == doc[0]:
                            doc_tf = item[1]
                            break
                    doc_tfidfs[doc[0]].append(doc_tf * idf1(len(doc_collection), len(inverted_index[term])))

    similarity = {}
    for doc in doc_tfidfs:
        similarity[doc] = cosine_similarity(query_tfidfs.values(), [doc_tfidfs[doc]])
    print(similarity)

    return placeholder


def run_vsm(doc_collection, queries, inverted_index):
    results = []

    results = vsm1(doc_collection, queries[0], inverted_index)

    # for query in queries:
    #     print(query)
    #     results = vsm1(doc_collection, query, inverted_index)
    #     elements = [int(item[0]) for item in results]
    #     results.append(elements)

    return results


