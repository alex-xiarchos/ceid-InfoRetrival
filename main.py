import inverted_index as ii
import vector_space_model as vsm


def main_app():
    sorted_inverted_index, total_words = ii.create_inverted_index()
    query_sentence = 0
    word_dict = ii.create_word_dict(total_words, sorted_inverted_index, query_sentence)

    docs_tf = vsm.get_tf_dict(sorted_inverted_index)
    docs_idfs = vsm.get_idf_dict(docs_tf)
    docs_tfidfs = vsm.get_tfidf(docs_tf, docs_idfs, word_dict)
    magnitudes, q_dot_magn = vsm.magnitudes_calc(docs_tfidfs)
    vsm.cos_calc(magnitudes, q_dot_magn)



if __name__ == '__main__':
    main_app()
