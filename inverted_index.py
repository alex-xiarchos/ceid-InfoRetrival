def create_inverted_index(stripped_docs_tuples):
    inverted_index = {}

    for doc_tuple in stripped_docs_tuples:
        for term in doc_tuple[1]:
            if term not in inverted_index:
                inverted_index[term] = set()
            inverted_index[term].add((doc_tuple[0], doc_tuple[1].count(term)))

    return inverted_index
