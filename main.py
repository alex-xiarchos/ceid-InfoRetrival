import inverted_index
import vector_space_model


def main_app():
    sorted_inverted_index, total_words = inverted_index.create_inverted_index()
    query_sentence = 0
    word_dict = inverted_index.create_word_dict(total_words, sorted_inverted_index, query_sentence)

    docs_tf = vector_space_model.get_tf_dict(sorted_inverted_index)
    docs_idfs = vector_space_model.get_idf_dict(docs_tf)
    docs_tfidfs = vector_space_model.get_tfidf(docs_tf, docs_idfs, word_dict)

    # queries = tools.get_queries()
    # queries_dict = dict.fromkeys(queries, 1)
    # queries_tf = vector_space_model.get_tf_dict(queries_dict)
    # queries_idfs = vector_space_model.get_idf_dict(queries_dict)


if __name__ == '__main__':
    main_app()
