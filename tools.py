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


def get_queries():
    filename = 'Collection/Queries_20'

    query_list = []

    with open(filename, 'r') as queries_file:
        query = queries_file.readlines()
        query_list.append(query)

    return query