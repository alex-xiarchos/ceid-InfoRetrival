import math
import numpy as np

TOTAL_NUMBER_OF_DOCS = 1240
FILTERED_NUMBER_OF_DOCS = 1209


def get_doc_tf(inverted_index):
    # dictionary με το πλήθος των εμφανίσεων (tf) κάθε λήμματος σε όλα τα έγγραφα -> 'λήμμα' = x αριθμός εμφανίσεων
    word_occur_total = {}

    # λίστα με το πλήθος εμφανίσεων λημμάτων για κάθε έγγραφο
    word_occur_docs = [{} for _ in range(1, TOTAL_NUMBER_OF_DOCS + 1)]

    # Αρχικοποίηση word_occur_total:
    word_occur_total = dict.fromkeys(inverted_index.keys(), 0)

    for key, value in inverted_index.items():
        word_occur_total[key] = len(set(value))

    # Αρχικοποίηση word_occur_docs:
    for i in range(1, TOTAL_NUMBER_OF_DOCS):
        word_occur_docs[i] = dict.fromkeys(inverted_index.keys(), 0)

    for term, doc_list in inverted_index.items():
        for doc in doc_list:
            word_occur_docs[doc][term] += 1

    max_tf = [0 for _ in range(1, TOTAL_NUMBER_OF_DOCS + 1)]

    for i in range(1, TOTAL_NUMBER_OF_DOCS):
        max_tf[i] = max(word_occur_docs[i].values())

    tf_dicts = word_occur_docs

    # Κανονικοποίηση βάσει του 0.5 + 0.5*(tf/max(tf))
    for i in range(1, TOTAL_NUMBER_OF_DOCS):
        for term in inverted_index.keys():
            if max_tf[i] == 0:  # για τα έγγραφα που δεν υπάρχουν ως νούμερο
                tf_dicts[i][term] = 0
            else:
                tf_dicts[i][term] = 0.5 + 0.5 * (word_occur_docs[i][term] / max_tf[i])

    return tf_dicts, word_occur_total, word_occur_docs


def get_doc_idf(word_occur_total):
    idf_dict = word_occur_total

    for key, value in word_occur_total.items():
        idf_dict[key] = np.log10(FILTERED_NUMBER_OF_DOCS / float(value))

    return idf_dict


def get_doc_tfidf(tf_dicts, idf_dict):
    tfidf_dicts = [{} for _ in range(1, TOTAL_NUMBER_OF_DOCS + 1)]

    for doc_index, tf_dict in enumerate(tf_dicts):
        for term, tf_value in tf_dict.items():
            tfidf = tf_value * idf_dict.get(term, 0)
            tfidf_dicts[doc_index][term] = tfidf

    return tfidf_dicts


def get_magnitudes(tfidf_dicts):
    magnitudes = []
    sums = 0

    # Στη vsm_sqrts λίστα αποθηκεύεται το ευκλείδειο διάνυσμα όλων των τιμών
    # Στη 0η τιμή είναι η τιμή του query.
    for i in range(0, TOTAL_NUMBER_OF_DOCS):
        for key, value in tfidf_dicts[i].items():
            sums += pow(value, 2)
        magnitudes.append(math.sqrt(sums))
        sums = 0

    q_dot_magn = []
    q_dot_magn.append(0) # Θέτουμε ως 0 την τιμή των queries

    for i in range(1, 1240):
        for key, value in tfidf_dicts[i].items():
            if tfidf_dicts[0][key] != 0 and tfidf_dicts[i][key] != 0:
                sums += tfidf_dicts[0][key] * tfidf_dicts[i][key]     # Q * Di
        q_dot_magn.append(sums)
        sums = 0

    return magnitudes, q_dot_magn


def cos_calc(magnitudes, q_dot_magn):
    cosines = []

    for i in range(1, 1240):
        cosines.append(math.cos(q_dot_magn[i] / (magnitudes[0] * magnitudes[i] + 0.0000001)))

    for i, value in enumerate(cosines):
        print(i, value)

    print(max(cosines))