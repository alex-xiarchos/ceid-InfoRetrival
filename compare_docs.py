import inverted_index
import csv


def compare_doc_lengths():
    with open('doc_lengths', 'w'): pass # Καθαρίζω το αρχείο

    doc_lengths = {}
    for doc_index in range(1, 1239):
        doc_path = inverted_index.get_doc_path(doc_index)

        try:
            with open(doc_path, "r") as file:
                doc = file.readlines()

            # Remove "\n" from words
            for index, word in enumerate(doc):
                doc[index] = inverted_index.remove_pattern_from_string(doc[index], r"\n")

            doc_length = 0
            for i, doc in enumerate(doc):
                for term in doc.split():
                    doc_length += 1

            doc_lengths[doc_index] = doc_length
            print(f"Το έγγραφο {doc_index} έχει μήκος {doc_length}.")


        except FileNotFoundError:
            print(f"ΔΕΝ ΥΠΑΡΧΕΙ ΑΡΧΕΙΟ ΜΕ ΝΟΥΜΕΡΟ {doc_index}.")

        finally:
            with open('doc_lengths.csv', 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the header
                writer.writerow(['Doc', 'Length'])

                # Write the transposed data
                for key, value in doc_lengths.items():
                    writer.writerow([key, value])