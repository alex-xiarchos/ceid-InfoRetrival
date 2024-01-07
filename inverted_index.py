import tools


def create_inverted_index():
    inverted_index = {}
    total_words = set()
    word_dict = {}

    for doc_number in range(1, 1240):  # 1239 έγγραφα????????????
        doc = tools.get_doc(doc_number)
        try:
            for doc_content in doc:  # Το doc βρίσκεται σε μορφή list, το doc_content το χωρίζει σε λέξεις.
                for doc_word in doc_content.split():
                    total_words.add(doc_word)

            print(f"Διαβάζονται {doc_number}/1239 έγγραφα για την συλλογή των λέξεων")
        except TypeError:
            pass

    for i in range(1240):
        word_dict[i] = dict.fromkeys(total_words, 0)

    for doc_number in range(1, 1240):  # 1239 έγγραφα
        doc = tools.get_doc(doc_number)

        try:
            for doc_content in doc:  # Το doc βρίσκεται σε μορφή list, το doc_content το χωρίζει σε λέξεις.
                for doc_word in doc_content.split():
                    # Δημιουργία inverted index
                    if doc_word in inverted_index:
                        inverted_index[doc_word].add(doc_number)
                    else:
                        inverted_index[doc_word] = {doc_number}
                    word_dict[doc_number][doc_word] += 1

            print(f"Διαβάζονται {doc_number}/1239 έγγραφα για τη δημιουργία του ανεστραμμένου ευρετηρίου")
        except TypeError:
            pass

    sorted_inverted_index = dict(sorted(inverted_index.items()))
    print("Το ανεστραμμένο ευρετήριο δημιουργήθηκε.")

    return sorted_inverted_index, word_dict
