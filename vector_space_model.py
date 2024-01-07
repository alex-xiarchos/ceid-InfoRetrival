import math


def get_tf_dict(word_dict):
    tf_dict = {}
    for word, count in word_dict.items():
        tf_dict[word] = count / float(1239)
    return tf_dict


def get_idf_dict(word_dict):
    idf_dict = {}

    idf_dict = dict.fromkeys(word_dict.keys(), 0)
    for word, val in idf_dict.items():
        idf_dict[word] = math.log10(1209 / (float(val) + 1))

    return idf_dict


def get_tfidf(tf, idfs):
    tfidf = {}
    for word, val in tf.items():
        tfidf[word] = val * idfs[word]

    return tfidf
