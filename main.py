import inverted_index as ii
import vector_space_model as vsm
import preprocessing as prep


def main_app():
    prep.preprocess_collection()
    prep.preprocess_queries()

    inverted_index = ii.create_inverted_index()

    # tf_dicts, word_occur_total, word_occur_docs = vsm.get_doc_tf(sorted_inverted_index)
    # idf_dict = vsm.get_doc_idf(word_occur_total)
    # docs_tfidfs = vsm.get_tfidf(tf_dicts, idf_dict)
    # magnitudes, q_dot_magn = vsm.get_magnitudes(docs_tfidfs)
    # vsm.cos_calc(magnitudes, q_dot_magn)


if __name__ == '__main__':
    main_app()
