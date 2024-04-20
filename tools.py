import os


def get_docs():
    docs_directory = 'Collection/docs'
    filename_list = [file for file in os.listdir(docs_directory)]

    doc_tuples_list = []

    for filename in filename_list:
        with open(os.path.join(docs_directory, filename), 'r') as doc_file:
            doc = doc_file.readlines()
            doc = [word.strip() for word in doc]
            doc_tuple = (filename, doc) # (DocID, <doc>)
            doc_tuples_list.append(doc_tuple)

    return doc_tuples_list


def get_queries():
    filename = 'Collection/Queries_20'

    with open(filename, 'r') as queries_file:
        queries = queries_file.readlines()

    return queries
