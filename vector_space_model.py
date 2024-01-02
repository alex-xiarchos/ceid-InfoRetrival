import csv
import ast


def get_term_frequencies():
    with open("sorted_inverted_index.csv", 'r') as file:
        csv_reader = csv.reader(file)

        term_frequency_dict = {}

        for index, row in enumerate(csv_reader):
            if index != 0:
                term = row[0]   # κάθε λήμμα
                term_instances_set = ast.literal_eval(row[1])   # μετατροπή του string του csv σε κανονικό set
                instances = 0   # ο counter που θα μετράει το term frequency για κάθε λήμμα
                for tuple in term_instances_set:
                    doc_of_term = tuple[1] # αριθμός εγγράφου όπου περιλαμβάνεται το λήμμα
                    instances += 1
                term_frequency_dict[term] = instances

    for term, tf in term_frequency_dict.items():
        print(f"{term}: {tf}")

    return term_frequency_dict

def calculate_tfidf():
    get_term_frequencies()