import csv
import ast
import math


def get_term_frequencies():
    with open("sorted_inverted_index.csv", 'r') as inverted_index_file:
        csv_reader = csv.reader(inverted_index_file)

        term_frequency_dict = {}

        for index, row in enumerate(csv_reader):
            if index != 0:
                term = row[0]  # κάθε λήμμα
                term_instances_set = ast.literal_eval(row[1])  # μετατροπή του string του csv σε κανονικό set
                instances = 0  # ο counter που θα μετράει το term frequency για κάθε λήμμα
                for tuple in term_instances_set:
                    doc_of_term = tuple[1]  # αριθμός εγγράφου όπου περιλαμβάνεται το λήμμα
                    instances += 1
                term_frequency_dict[term] = instances

    # for term, tf in term_frequency_dict.items():
    #     print(f"{term}: {tf}")
    print("(Term Frequencies computed)\n")
    return term_frequency_dict


def calculate_query_tf(query_row_index_to_get):

    # Ανάγνωση queries
    with open("/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Documents/CEID/ΕΠΙΛΟΓΕΣ ΧΕΙΜΕΡΙΝΟΥ/ΑΝΑΚΤΗΣΗ "
              "ΠΛΗΡΟΦΟΡΙΑΣ/PROJECT/Collection/Queries_20", 'r') as query_file:
        for query_row_index, query_row in enumerate(query_file):
            if query_row_index == query_row_index_to_get:
                print(query_row_index, query_row)

                # Tokenize and convert query to lowercase
                query_terms = query_row.upper().split()
                query_term_frequency_dict = {}

                # Calculate TF-IDF scores for the query
                for term in query_terms:
                    # Calculate Term Frequency (TF) for the query
                    query_tf = query_terms.count(term) / len(query_terms)
                    query_term_frequency_dict[term] = query_tf

                # for term, tf in query_term_frequency_dict.items():
                #     print(f"{term}: {tf}")
                print("(Query Term Frequencies computed)\n")

                return query_term_frequency_dict



def calculate_tfidf():
    term_frequency_dict = get_term_frequencies()
    query_term_frequency_dict = calculate_query_tf(0)
    tfidf_scores = {}

    # Calculate Inverse Document Frequency (IDF)
    for term in query_term_frequency_dict:
        idf = math.log10(1209 / (query_term_frequency_dict[term]))
        print(f"{term} -> {query_term_frequency_dict[term]} -> {idf}")

        # Calculate TF-IDF for the query
        tfidf_scores[term] = term_frequency_dict[term] * idf

    print()
    for term, tfidf in tfidf_scores.items():
        print(f"{term} -> {tfidf}")

    return tfidf_scores