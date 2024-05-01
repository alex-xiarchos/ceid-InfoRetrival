import json
import os


def get_docs():
    docs_directory = 'Collection/docs'
    filename_list = [file for file in os.listdir(docs_directory)]

    doc_tuples_list = []

    for filename in filename_list:
        with open(os.path.join(docs_directory, filename), 'r') as doc_file:
            doc = doc_file.readlines()
            doc = [word.strip() for word in doc]
            doc_tuple = (filename, doc)  # (DocID, <doc>)
            doc_tuples_list.append(doc_tuple)

    return doc_tuples_list


def get_queries():
    filename = 'Collection/Queries_20'

    with open(filename, 'r') as queries_file:
        queries = queries_file.readlines()

    return queries


def get_json_file(json_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    return json_data


def get_relevant():
    relevant_docs = {}
    with open('Collection/Relevant_20', 'r') as file:
        for i, line in enumerate(file):
            relevant_docs[i] = [int(item) for item in line.split()]

    return relevant_docs
