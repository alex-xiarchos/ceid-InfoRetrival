import inverted_index
import vector_space_model
import pandas as pd


def main_app():
    sorted_inverted_index, word_dict = inverted_index.create_inverted_index()
    tf_first = vector_space_model.get_idf_dict(word_dict[2])
    idfs = vector_space_model.get_idf_dict(word_dict[1])
    print(idfs)
    # compare_docs.compare_doc_lengths()


if __name__ == '__main__':
    main_app()
