import json
from collections import defaultdict


def create_inverted_index():
    inverted_index = {}
    index_value = {}

    with open('stripped_docs_tuples.json', 'r') as stripped_docs_file:
        stripped_docs_tuples = json.load(stripped_docs_file)

    for doc_tuple in stripped_docs_tuples:
        for term in doc_tuple[1]:
            if term not in inverted_index:
                inverted_index[term] = set()
            inverted_index[term].add((doc_tuple[0], doc_tuple[1].count(term)))

    print(inverted_index)
    return inverted_index