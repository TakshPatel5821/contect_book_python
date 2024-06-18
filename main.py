from pythonproj import input_data, data_search, view_all, update_rec, delete_rec


def main():
    """This function calls functions from the pythonproj.py file and executes based on user input"""
    while True:
        x = input("1. Create new contact\t\t2. Search data\t\t3. Update Record\t\t4. Delete Record\t\t"
                  "5.View all records\n6. Exit\n")
        if x == '1':
            input_data()
        elif x == '2':
            data_search()
        elif x == '3':
            update_rec()
        elif x == '4':
            delete_rec()
        elif x == '5':
            view_all()
        else:
            print("Thank you!")
            break


if __name__ == '__main__':
    """The main function calls the main() function"""
    main()
