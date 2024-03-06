import tools


def create_inverted_index():
    # δημιουργούμε ένα αρχικό dictionary όπου θα αποτελέσει το ευρετήριο που θα αποθηκευτούν αρχικά οι λέξεις
    inverted_index = {}

    # Δημιουργία inverted index:
    for doc_number in range(1, 1240):  # 1239 έγγραφα ξεκινώντας από το 1
        doc = tools.get_doc(doc_number)

        try:
            for doc_word in doc:  # κάθε λέξη του εγγράφου
                if doc_word in inverted_index:
                    inverted_index[doc_word].append(doc_number)
                else:
                    inverted_index[doc_word] = [doc_number]

            # print(f"Διαβάζονται {doc_number}/1239 έγγραφα για τη δημιουργία του ανεστραμμένου ευρετηρίου")
        except TypeError:
            pass

    inverted_index.pop("") # αφαιρεί άδεια strings που προκύπτουν από τις κενές γραμμές στο τέλος των documents

    sorted_inverted_index = dict(sorted(inverted_index.items()))
    print("> Το ανεστραμμένο ευρετήριο δημιουργήθηκε.")

    return sorted_inverted_index


# Χρειάζεται;;;
def create_word_dict(inverted_index, query_sentence):
    word_dict = {}

    # Αρχικοποίηση λίστας με word_dicts
    for doc_number in range(0, 1240):
        word_dict[doc_number] = {key: 0 for key in inverted_index.keys()}

    # Για κάθε τιμή του inverted_index, πηγαίνω στην αντίστοιχη γραμμή του word_dict
    # και προσθέτω +1 στην αντίστοιχη λέξη.
    for key, value in inverted_index.items():
        for doc_number in value:
            word_dict[doc_number][key] += 1
            # print(f"key = {key}, value = {value}. doc_number = {doc_number}")
            # print(f"word_dict[{doc_number}][{key}] = {word_dict[doc_number][key]}")

    queries = tools.get_queries()
    for query_word in queries[query_sentence].split(' '):
        if query_word in word_dict[0]:
            word_dict[0][query_word] += 1
        else:
            word_dict[0][query_word] = 1

    return word_dict
