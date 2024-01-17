import inverted_index
import tools
import vector_space_model


def main_app():
    sorted_inverted_index, total_words = inverted_index.create_inverted_index()
    print(sorted_inverted_index)
    word_dict = inverted_index.create_word_dict(total_words, sorted_inverted_index)

    for key, value in word_dict[1].items():
        if value != 0 and value != 1:
            print(key, value)


    # docs_tf = vector_space_model.get_tf_dict(word_dict[1])  # dict[1] = πρώτο document
    # docs_idfs = vector_space_model.get_idf_dict(word_dict[1])
    # docs_tfidfs = vector_space_model.get_tfidf(docs_tf, docs_idfs)

    # queries = tools.get_queries()
    # queries_dict = dict.fromkeys(queries, 1)
    # queries_tf = vector_space_model.get_tf_dict(queries_dict)
    # queries_idfs = vector_space_model.get_idf_dict(queries_dict)

    # Πρέπει να φτιαχτούν τα queries, να ολοκληρωθεί το vector space model και μετά (3), (4).
    # Ίσως χρειάζεται αναδιοργάνωση των συναρτήσεων από την αρχή για να ενσωματωθούν τα queries.

if __name__ == '__main__':
    main_app()
