import tools
import matplotlib.pyplot as plt
import numpy as np


def recall_precision(results, model):
    # results: λίστα (όλων των queries) που περιλαμβάνει λίστες με τα πιο σχετικά έγγραφα, όπως υπολογίστηκαν από το cosine similarity
    relevant_docs = tools.get_relevant()
    # relevant_docs: dictionary με τις τιμές των πραγματικά σχετικών εγγράφων του Relevent_20

    recall_precision_values = []

    if model == "vsm":
        # Το results περιλαμβάνει συγκεντρωτικά όλα τα αποτελέσματα για κάθε query. Διατρέχουμε το κάθε query μεμονομένα...
        for i, results_query in enumerate(results):
            precision = []
            recall = []
            truly_relevant_docs = 0
            # διατρέχουμε τα πιο σχετικά έγγραφα για το συγκεκριμένο query...
            for j, doc in enumerate(results[i]):
                if type(doc) == tuple:
                    current_doc = int(doc[0])
                    if current_doc in relevant_docs[i]:
                        truly_relevant_docs += 1

                        recall.append(truly_relevant_docs / len(results_query))
                        precision.append(truly_relevant_docs / (j + 1))

            recall_precision_values.append((recall, precision))

    if model == "colBERT":
        for i, results_query in enumerate(results):
            precision = []
            recall = []
            truly_relevant_docs = 0
            for j, doc in enumerate(results[i]):
                if doc in relevant_docs[i]:
                    truly_relevant_docs += 1

                    recall.append(truly_relevant_docs / len(results_query))
                    precision.append(truly_relevant_docs / (j + 1))

            recall_precision_values.append((recall, precision))

    return recall_precision_values


def mean_average_precision(recall_precision_values):
    average_precision_list = []
    for i in range(len(recall_precision_values)):
        recalls, precisions = recall_precision_values[i]
        average_precision = 0

    for j in range(1, len(recalls)):
        average_precision += (recalls[j] - recalls[j - 1]) * precisions[j]
        average_precision_list.append(average_precision)

    return np.mean(average_precision_list)


def run_metrics(vsm1_results, vsm2_results):
    colBERT_results = tools.get_json_file("colBERT_output.json")

    recall_precision_vsm1 = recall_precision(vsm1_results, "vsm")
    recall_precision_vsm2 = recall_precision(vsm2_results, "vsm")
    recall_precision_colBERT = recall_precision(colBERT_results, "colBERT")

    map_vm1 = mean_average_precision(recall_precision_vsm1)
    map_vm2 = mean_average_precision(recall_precision_vsm2)
    map_colBERT = mean_average_precision(recall_precision_colBERT)

    print("vm1", map_vm1)
    print("vm2", map_vm2)
    print("colBERT", map_colBERT)

    for i in range(len(recall_precision_vsm1)):
        plt.figure()
        plt.plot(recall_precision_vsm1[i][0], recall_precision_vsm1[i][1], label="VSM 1")
        plt.plot(recall_precision_vsm2[i][0], recall_precision_vsm2[i][1], label="VSM 2")
        plt.plot(recall_precision_colBERT[i][0], recall_precision_colBERT[i][1], label="colBERT")
        plt.xlabel('Ανάκληση')
        plt.ylabel('Ακρίβεια')
        plt.title(f'Ερώτημα {i + 1}')
        plt.legend(loc='upper right')
        plt.savefig('Precision_Recall_Curve/' + str(i + 1) + '.png')
