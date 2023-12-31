import inverted_index


def main_app():
    while True:
        print("Select 1 for inverted index Creation")
        print("Select 2 for Vector Space Model")
        print("Select 0 to exit")
        choice = int(input("SELECT: "))

        if choice == 1:
            inverted_index.create_inverted_index()
            inverted_index.print_inverted_index()
        elif choice == 2:
            pass
        elif choice == 0:
            break
        else:
            print("WRONG CHOICE! \n")


if __name__ == '__main__':
    main_app()
