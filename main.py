import inverted_index as ii
import vector_space_model as vsm
import preprocessing as prep


def main_app():
    doc_collection = prep.preprocess_collection()   # stripped_docs
    queries = prep.preprocess_queries()     # stripped_queries

    inverted_index = ii.create_inverted_index(doc_collection)
    results = vsm.run_vsm(doc_collection, queries, inverted_index)

    # idf_dict = vsm.get_doc_idf(word_occur_total)
    # docs_tfidfs = vsm.get_tfidf(tf_dicts, idf_dict)
    # magnitudes, q_dot_magn = vsm.get_magnitudes(docs_tfidfs)
    # vsm.cos_calc(magnitudes, q_dot_magn)


if __name__ == '__main__':
    main_app()
