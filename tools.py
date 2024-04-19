import re
import os


def get_docs():
    docs_directory = 'Collection/docs'
    filename_list = [file for file in os.listdir(docs_directory)]

    doc_list = []

    for filename in filename_list:
        with open(os.path.join(docs_directory, filename), 'r') as doc_file:
            doc = doc_file.readlines()
            doc = [word.strip() for word in doc]
            doc_list.append(doc)

    return doc_list


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