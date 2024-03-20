import math
import numpy as np

GROSS_NUMBER_OF_DOCS = 1240
NET_NUMBER_OF_DOCS = 1209


def get_tf_dicts(inverted_index):
    # dictionary με το πλήθος των εμφανίσεων (tf) κάθε λήμματος σε όλα τα έγγραφα -> 'λήμμα' = x αριθμός εμφανίσεων
    word_occur_total = {}

    # λίστα με το πλήθος εμφανίσεων λημμάτων για κάθε έγγραφο
    word_occur_docs = [{} for _ in range(1, GROSS_NUMBER_OF_DOCS + 1)]

    # Αρχικοποίηση word_occur_total:
    word_occur_total = dict.fromkeys(inverted_index.keys(), 0)

    for key, value in inverted_index.items():
        word_occur_total[key] = len(set(value))

    # Αρχικοποίηση word_occur_docs:
    for i in range(1, GROSS_NUMBER_OF_DOCS):
        word_occur_docs[i] = dict.fromkeys(inverted_index.keys(), 0)

    for term, doc_list in inverted_index.items():
        for doc in doc_list:
            word_occur_docs[doc][term] += 1

    max_tf = [0 for _ in range(1, GROSS_NUMBER_OF_DOCS + 1)]

    for i in range(1, GROSS_NUMBER_OF_DOCS):
        max_tf[i] = max(word_occur_docs[i].values())

    tf_dicts = word_occur_docs

    # Κανονικοποίηση βάσει του 0.5 + 0.5*(tf/max(tf))
    for i in range(1, GROSS_NUMBER_OF_DOCS):
        for term in inverted_index.keys():
            if max_tf[i] == 0:  # για τα έγγραφα που δεν υπάρχουν ως νούμερο
                tf_dicts[i][term] = 0
            else:
                tf_dicts[i][term] = 0.5 + 0.5 * (word_occur_docs[i][term] / max_tf[i])

    return tf_dicts, word_occur_total


def get_idf_dict(word_occur_total):
    idf_dict = word_occur_total

    for key, value in word_occur_total.items():
        idf_dict[key] = np.log10(NET_NUMBER_OF_DOCS / float(value))

    return idf_dict


def get_tfidf(tf, idfs, word_dict):
    tfidf_values = {}
    for key, value in tf.items():
        tfidf_values[key] = value * idfs[key]

    # Δημιουργία dictionary όπου σε κάθε εμφάνιση της λέξης, αποθηκεύεται το weight της.
    # Χρησιμοποιούμε το word_dict ως βάση, γιατί ήδη έχει μηδενικά εκεί όπου δεν εμφανίζεται η λέξη.
    tfidf_dict = []
    tfidf_dict = word_dict

    for i in range(0, 1240):
        for key, value in tfidf_dict[i].items():
            if value > 1:
                tfidf_dict[i][key] = 1

    # Πλέον στο tfidf_dict, όλες οι εμφανίσεις των λέξεων αποθηκεύονται ως 1.
    # Μένει να πολλαπλασιαστούν με τα βάρη που αποθηκεύσαμε στο tfidf_values.
    for i in range(0, 1240):
        for key in tfidf_dict[i]:
            tfidf_dict[i][key] *= tfidf_values[key]

    for key, value in tfidf_dict[1].items():
        if value != 0:
            print(key, value)

    return tfidf_dict


def magnitudes_calc(tfidf_dict):
    magnitudes = []
    sums = 0

    # Στη vsm_sqrts λίστα αποθηκεύεται το ευκλείδειο διάνυσμα όλων των τιμών
    # Στη 0η τιμή, όπως πάντα, είναι η τιμή του query.
    for i in range(0, 1240):
        for key, value in tfidf_dict[i].items():
            sums += pow(value, 2)
        magnitudes.append(math.sqrt(sums))
        sums = 0

    q_dot_magn = []
    q_dot_magn.append(0) # Θέτουμε ως 0 την τιμή των queries

    for i in range (1, 1240):
        for key, value in tfidf_dict[i].items():
            if tfidf_dict[0][key] != 0 and tfidf_dict[i][key] != 0:
                sums += tfidf_dict[0][key] * tfidf_dict[i][key]     # Q * Di
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