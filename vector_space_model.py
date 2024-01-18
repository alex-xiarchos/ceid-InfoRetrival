import math


def get_tf_dict(sorted_inverted_index):
    tf_dict = {}

    # Αρχικοποίηση tf_dict με όλες τις πιθανές λέξεις.
    for i in range(1, 1240):
        tf_dict = dict.fromkeys(sorted_inverted_index.keys(), 0)

    # Σε κάθε λέξη του tf_dict αποθηκεύεται ο συνολικός αριθμός των εμφανίσεων
    # από τις λέξεις στο inverted index.
    for key, value in sorted_inverted_index.items():
        tf_dict[key] = len(value)

    return tf_dict


def get_idf_dict(tf_dict):
    idf_dict = tf_dict

    for key, value in idf_dict.items():
        idf_dict[key] = math.log10(1209 / (float(value) + 1))

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

    return tfidf_values
