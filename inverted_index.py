import re

# Αφαίρεση των \n χαρακτήρων από τα docs χρησιμοποιώντας regex
def remove_pattern_from_string(text, pattern):
    replacement = ""
    modified_text = re.sub(pattern, replacement, text)
    return modified_text


# Εισάγεται ένας αριθμός (1-1239) και επιστρέφεται το path του αρχείου με αυτό το νούμερο
# Δεν υπάρχει ανάγκη για έλεγχο του range του αριθμού, μιας και ελέγχονται τα exceptions
def get_doc_path(number):
    file_path_prefix = "/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Documents/CEID/ΕΠΙΛΟΓΕΣ ΧΕΙΜΕΡΙΝΟΥ/ΑΝΑΚΤΗΣΗ ΠΛΗΡΟΦΟΡΙΑΣ/PROJECT/Collection/docs/"
    file_path_suffix = str(number).zfill(5)  # 1 -> 00001
    file_path = file_path_prefix + file_path_suffix
    return file_path


def create_inverted_index():
    inverted_index = {}
    total_words = set()
    word_dict = {}

    for doc_number in range(1, 1240):  # 1239 έγγραφα
        doc = get_doc(doc_number)
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
        doc = get_doc(doc_number)

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


# Δίνεις 5 και επιστρέφεται μια λίστα με το περιεχόμενο του εγγράφου 00005
def get_doc(doc_number):
    doc_path = get_doc_path(doc_number)  # Ανοίγεται το κάθε doc ξεχωριστά

    try:
        with open(doc_path, "r") as doc_file:
            doc = doc_file.readlines()  # ανάγνωση document

        # Αφαίρεση "\n" χαρακτήρων από το περιεχόμενο του document
        for index, word in enumerate(doc):
            doc[index] = remove_pattern_from_string(doc[index], r"\n")

        return doc

    except FileNotFoundError:
        pass
