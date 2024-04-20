import json

def create_inverted_index():
    inverted_index = {}

    with open('stripped_docs_tuples.json', 'r') as stripped_docs_file:
        stripped_docs_tuples = json.load(stripped_docs_file)



    # for docID in range(1, TOTAL_NUMBER_OF_DOCS):  # 1239 έγγραφα ξεκινώντας από το 1
    #     doc = tools.get_doc(docID)
    #
    #     try:
    #         for doc_word in doc:  # κάθε λέξη του εγγράφου
    #             if doc_word in inverted_index:
    #                 inverted_index[doc_word].append(docID)
    #             else:
    #                 inverted_index[doc_word] = [docID]
    #
    #         # print(f"Διαβάζονται {docID}/1239 έγγραφα για τη δημιουργία του ανεστραμμένου ευρετηρίου")
    #     except TypeError:
    #         pass

    # inverted_index.pop("")  # αφαιρεί άδεια strings που προκύπτουν από τις κενές γραμμές στο τέλος των documents

    # sorted_inverted_index = dict(sorted(inverted_index.items()))
    # print("> Το ανεστραμμένο ευρετήριο δημιουργήθηκε.")