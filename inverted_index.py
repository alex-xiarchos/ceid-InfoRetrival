import re
import csv
from beautifultable import BeautifulTable


def remove_pattern_from_string(text, pattern):
    replacement = ""
    modified_text = re.sub(pattern, replacement, text)
    return modified_text


def create_inverted_index():
    inverted_index = {}

    # Read from file
    file_path_prefix = "/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Documents/CEID/ΕΠΙΛΟΓΕΣ ΧΕΙΜΕΡΙΝΟΥ/ΑΝΑΚΤΗΣΗ ΠΛΗΡΟΦΟΡΙΑΣ/PROJECT/Collection/docs/"

    for file_index in range(1, 12):
        file_path_suffix = str(file_index).zfill(5)
        file_path = file_path_prefix + file_path_suffix

        try:
            with open(file_path, "r") as file:
                doc = file.readlines()

            # Remove "\n" from words
            for index, word in enumerate(doc):
                doc[index] = remove_pattern_from_string(doc[index], r"\n")

            # Create inverted index
            for i, doc in enumerate(doc):
                for term in doc.split():
                    if term in inverted_index:
                        inverted_index[term].add(tuple([file_index, i]))
                    else:
                        inverted_index[term] = {tuple([file_index, i])}

            print(f"{file_path_suffix} | {inverted_index}")


        except FileNotFoundError:
            print(f"ΔΕΝ ΥΠΑΡΧΕΙ ΑΡΧΕΙΟ ΜΕ ΝΟΥΜΕΡΟ {file_index}")

        finally:
            sorted_inverted_index = dict(sorted(inverted_index.items()))

            with open('sorted_inverted_index.csv', 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the header
                writer.writerow(['Key', 'Value'])

                # Write the transposed data
                for key, value in sorted_inverted_index.items():
                    writer.writerow([key, value])


def print_inverted_index():
    with open("sorted_inverted_index.csv", 'r') as file:
        reader = csv.reader(file)

        # Read header
        header = next(reader)

        # Create BeautifulTable with header
        table = BeautifulTable()
        table.column_headers = header

        # Read and add rows to the table
        for row in reader:
            table.append_row(row)

        table.column_widths = [30, 70]

        print(table)