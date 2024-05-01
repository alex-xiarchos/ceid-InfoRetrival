from icecream import ic
import tools
import matplotlib.pyplot as plt
import numpy as np


def recall_precision(results, model):
    # results: λίστα (όλων των queries) που περιλαμβάνει λίστες με τα πιο σχετικά έγγραφα, όπως υπολογίστηκαν από το cosine similarity
    relevant_docs = tools.return_relevant()
    # relevant_docs: dictionary με τις τιμές των πραγματικά σχετικών εγγράφων του Relevent_20

    recall_precision_values = []

    if model == "vsm":
        # διατρέχουμε τα αποτελέσματα για κάθε query...
        for i, results_query in enumerate(results):
            precision = []
            recall = []
            trully_relevant_docs = 0
            # διατρέχουμε τα πιο σχετικά έγγραφα για το συγκεκριμένο query...
            for j, doc in enumerate(results[i]):
                if type(doc) == tuple:
                    current_doc = int(doc[0])
                    if current_doc in relevant_docs[i]:
                        trully_relevant_docs += 1

                        recall.append(trully_relevant_docs / len(results_query))
                        precision.append(trully_relevant_docs / (j + 1))

            recall_precision_values.append((recall, precision))

    if model == "colBERT":
        # διατρέχουμε τα αποτελέσματα για κάθε query...
        for i, results_query in enumerate(results):
            precision = []
            recall = []
            trully_relevant_docs = 0
            # διατρέχουμε τα πιο σχετικά έγγραφα για το συγκεκριμένο query...
            for j, doc in enumerate(results[i]):
                if doc in relevant_docs[i]:
                    trully_relevant_docs += 1

                    recall.append(trully_relevant_docs / len(results_query))
                    precision.append(trully_relevant_docs / (j + 1))

            recall_precision_values.append((recall, precision))

    return recall_precision_values


def mean_average_precision(recall_precision_values):
    average_precision_list = []
    for i in range(len(recall_precision_values)):
        recalls, precisions = recall_precision_values[i]
        average_precision = 0

    for j in range(1, len(recalls)):
        average_precision += (recalls[j] - recalls[j-1]) * precisions[j]
        average_precision_list.append(average_precision)

    return np.mean(average_precision_list)


def run_metrics(vsm1_results, vsm2_results):
    colBERT_results = tools.return_json("colBERT_output.json")

    recall_precision_vsm1 = recall_precision(vsm1_results, "vsm")
    recall_precision_vsm2 = recall_precision(vsm2_results, "vsm")
    recall_precision_colBERT = recall_precision(colBERT_results, "colBERT")

    map_vm1 = mean_average_precision(recall_precision_vsm1)
    map_vm2 = mean_average_precision(recall_precision_vsm2)
    map_colBERT = mean_average_precision(recall_precision_colBERT)

    ic(map_vm1)
    ic(map_vm2)
    ic(map_colBERT)

    for i in range(len(recall_precision_vsm1)):
        plt.figure()
        plt.plot(recall_precision_vsm1[i][0], recall_precision_vsm1[i][1], label="VSM 1")
        plt.plot(recall_precision_vsm2[i][0], recall_precision_vsm2[i][1], label="VSM 2")
        plt.plot(recall_precision_colBERT[i][0], recall_precision_colBERT[i][1], label="colBERT")
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title(f'Precision-Recall Curve for Query {i + 1}')
        plt.legend(loc='upper right')
        plt.savefig('Precision_Recall_Curve/' + str(i + 1) + '.png')