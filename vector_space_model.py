import math
from sklearn.metrics.pairwise import cosine_similarity


def query_weight_1(tf, idf, term):
    return (0.5 + (0.5*tf[term])/tf[max(tf)]) * idf


def query_weight_2(tf, idf, term):
    return (0.5 + (0.5*tf[term])/tf[max(tf)]) * idf


def doc_weight_1(tf, idf):
    return tf*idf


def doc_weight_2(tf, idf, term):
    return 0.5 + (0.5*tf[term])/tf[max(tf)]


def idf1(N, n):
    return math.log(N/n)


def idf2():
    return math.log(1 + N/n)


def vsm(doc_collection, query, inverted_index):
    placeholder = []

    # dictionary με τις f τιμές του ερωτήματος
    f = {}
    for term in query:
        f[term] = query.count(term)

    # dictionary με keys τα docID και values lists που αντιστοιχούν στα ??????? ('docID': [])
    tf_idf_docs = {}
    for doc in doc_collection:
        tf_idf_docs[doc[0]] = []

    # ?????????
    tf_idf_queries = []

    for term in query:
        if term in inverted_index:
            # υπολογισμός idf τιμής για το συγκεκριμένο term
            idf = idf1(len(doc_collection), len(inverted_index[term]))
            # υπολογισμός tf-idf τιμής για το συγκεκριμένο term (βάρος όρου ερωτήματος) και αποθήκευση
            tf_idf_queries.append(doc_weight_1(f[term], idf))

            tf_list = []    # περιλαμβάνει όλες τις tf τιμές για ένα συγκεκριμένο term όλων των docs

            # εύρεση και αποθήκευση των tf τιμών για το συγκεκριμένο term απ' όλα τα docs μέσω του inverted index
            for doc in doc_collection:
                for tuple_ in inverted_index[term]:
                    tf_list.append(tuple_[1])

                # υπολογισμός tf-idf τιμής βάρος όρου εγγράφου για το συγκεκριμένο term και αποθήκευση
                for tf_value in tf_list:
                    w = tf_idf_docs(tf_value, idf, term)
                    tf_idf_docs[doc[0]].append(w)
                print(tf_idf_docs)

    # sim = {}
    # for doc in tf_idf_docs:
    #     sim[doc] = cosine_similarity([tf_idf_queries], [tf_idf_docs[doc]])
    #
    # return sorted(sim.items(), key=lambda x:x[1])[-500:][::-1]
    return placeholder


def run_vsm(doc_collection, queries, inverted_index):
    results = []

    for query in queries:
        print(query)
        results = vsm(doc_collection, query, inverted_index)
        elements = [int(item[0]) for item in results]
        results.append(elements)

    return results


