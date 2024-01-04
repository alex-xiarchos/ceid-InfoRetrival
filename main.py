import inverted_index
import vector_space_model
import compare_docs


def main_app():
    # # while True:
    #     print("Select 1 for Inverted Index creation")
    #     print("Select 2 for Vector Space Model")
    #     print("Select 9 for doc length comparison")
    #     print("Select 0 to exit")
        # choice = int(input("SELECT: "))
        choice = 2

        if choice == 1:
            inverted_index.create_inverted_index()
            inverted_index.print_inverted_index()
        elif choice == 2:
            vector_space_model.calculate_tfidf()
        elif choice == 9:
            compare_docs.compare_doc_lengths()
        # elif choice == 0:
        #     break
        # else:
        #     print("WRONG CHOICE! \n")


if __name__ == '__main__':
    main_app()
