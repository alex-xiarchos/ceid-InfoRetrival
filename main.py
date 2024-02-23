import inverted_index as ii
import vector_space_model as vsm


def main_app():
    sorted_inverted_index = ii.create_inverted_index()

    query_sentence = 0  # αριθμός πρότασης query
    word_dict = ii.create_word_dict(sorted_inverted_index, query_sentence)

    tf_dict, tf_dict_norm = vsm.get_tf_dict(sorted_inverted_index)
    idf_dict = vsm.get_idf_dict(tf_dict, tf_dict_norm)
    docs_tfidfs = vsm.get_tfidf(tf_dict, idf_dict, word_dict)
    magnitudes, q_dot_magn = vsm.magnitudes_calc(docs_tfidfs)
    # vsm.cos_calc(magnitudes, q_dot_magn)


if __name__ == '__main__':
    main_app()
