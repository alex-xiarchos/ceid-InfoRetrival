import re


# Αφαίρεση των \n χαρακτήρων από τα docs χρησιμοποιώντας regex
def remove_pattern_from_string(text, pattern):
    replacement = ""
    modified_text = re.sub(pattern, replacement, text)
    return modified_text


# Εισάγεται ένας αριθμός (1-1239) και επιστρέφεται το path του αρχείου με αυτό το νούμερο
# Δεν υπάρχει ανάγκη για έλεγχο του range του αριθμού, μιας και ελέγχονται τα exceptions
def get_doc_path(number):
    file_path_prefix = "Collection/docs/"
    file_path_suffix = str(number).zfill(5)  # 1 -> 00001
    file_path = file_path_prefix + file_path_suffix
    return file_path


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


def get_queries():
    file_path = "Collection/Queries_20"
    with open(file_path, 'r') as queries_file:
        queries = queries_file.readlines()

    # Αφαίρεση "\n" χαρακτήρων από το περιεχόμενο του document
    for index, query in enumerate(queries):
        queries[index] = remove_pattern_from_string(queries[index], r"\n")

    return queries
