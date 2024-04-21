


def vsm(doc_collection, query, inverted_index):
    placeholder = []
    tf_dictionary = {}

    # αρχικοποίηση tf_dictionary με τα keys-docID, κάθε key αντιστοιχεί σε ένα (κενό) list
    # for doc in doc_collection:
    #     tf_dictionary[doc[0]] = []

    for term in query:
        tf_dictionary[term] = query.count(term)

    print(tf_dictionary)

    return placeholder


def run_vsm(doc_collection, queries, inverted_index):
    results = []

    for query in queries:
        results = vsm(doc_collection, query, inverted_index)

    return results


