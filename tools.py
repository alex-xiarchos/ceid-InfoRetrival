import re


# Αφαίρεση των \n χαρακτήρων από τα docs χρησιμοποιώντας regex
def remove_pattern_from_string(text, pattern):
    replacement = ""
    modified_text = re.sub(pattern, replacement, text)
    return modified_text


# Εισάγεται ένας αριθμός (1-1239) και επιστρέφεται το path του αρχείου με αυτό το νούμερο
def get_doc_path(number):
    file_path_prefix = "Collection/docs/"
    file_path_suffix = str(number).zfill(5)  # 1 -> 00001
    file_path = file_path_prefix + file_path_suffix
    return file_path


# Δίνεις 5 και επιστρέφεται μια λίστα με το περιεχόμενο του εγγράφου 00005
def get_doc(doc_number):
    doc_path = get_doc_path(doc_number)  # το 5 μετατρέπεται σε 00005

    try:
        with open(doc_path, "r") as doc_file:
            doc = doc_file.readlines()  # γίνεται ανάγνωση του εγγράφου

        # Αφαίρεση "\n" χαρακτήρων από το περιεχόμενο του document
        for index, word in enumerate(doc):
            doc[index] = remove_pattern_from_string(doc[index], r"\n")

        return doc  # επιστρέφεται το έγγραφο

    except FileNotFoundError:
        pass


# Επιστρέφονται τα queries
def get_queries():
    file_path = "Collection/Queries_20"
    with open(file_path, 'r') as queries_file:
        queries = queries_file.readlines()

    queries_capped = [""] * 20  # αρχικοποίηση 20 άδειων strings

    # Αφαίρεση "\n" χαρακτήρων από το περιεχόμενο του document
    for index, query in enumerate(queries):
        queries[index] = remove_pattern_from_string(queries[index], r"\n")
        queries_capped[index] = queries[index].upper()  # αποθήκευση των queries αφού μετατραπούν σε κεφαλαία

    return queries_capped