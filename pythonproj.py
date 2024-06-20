import _sqlite3
mydb = _sqlite3.connect("contactbook.db")
cur = mydb.cursor()

create_table = "create table if not exists contacts_table(name varchar(30), number int(10), address varchar(40), " \
               "email varchar(30))"
cur.execute(create_table)


def input_data():
   
    name = input("Enter name:\n")
    number = input("Enter phone number:\n")
    address = input("Enter address:\n")
    email = input("Enter email id:\n")
    data_fetch = "select * from contacts_table where number = ?"
    cur.execute(data_fetch, (number,)) 
    result = cur.fetchall()
    if result:
        print("Number already exists. Please enter new")
    else:
        if name != "" or number != "" or address != "" or email != "":
            data_insert = "insert into contacts_table(name, number, address, email) values(?,?,?,?)"
            data = (name, number, address, email)
            cur.execute(data_insert, data)
            mydb.commit()
            print("Records saved!")
        else:
            print("Some field is empty, please enter again")


def data_search():
  
    choice = input("Search data based on: 1.Name\t2.Phone number\n")
    if choice == '1':
        name = input("Enter name of saved person: \n")
        data_fetch = "select * from contacts_table where name = ?"
        cur.execute(data_fetch, (name,))  
        result = cur.fetchall()  
    elif choice == '2':
        numb = input("Enter phone number of saved person: \n")
        data_fetch = "select * from contacts_table where number = ?"
        cur.execute(data_fetch, (numb,))
        result = cur.fetchall()
    else:
        print("Exited")
    if result:
        for res in result:
            print(res)
    else:
        print("Record not found")


def view_all():
   
    cur.execute("select * from contacts_table")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def update_rec():
   
    numb = input("Enter phone number of contact you'd like to update\n")
    data_fetch = "select * from contacts_table where number = ?"
    cur.execute(data_fetch, (numb,))  
    result = cur.fetchall()  
    if result:
        choice = input("What would you like to update?1.Name\t2.Phone number\t3.Address\t4.Email\t5.Exit")
        if choice == '1':
            newnm = input("Enter new name\n")
            data_update = "update contacts_table set name = ? where number = ?"
            values = (newnm, numb)
            cur.execute(data_update, values)
            mydb.commit()
            print("Record Updated!")
        elif choice == '2':
            newno = input("Enter new number\n")
            search_num = "select * from contacts_table where number = ?"
            cur.execute(search_num, (newno,))  # stored as tuple
            found = cur.fetchall()
            if found:
                print("Number already exists in contacts. Please enter a new number")
            else:
                data_update = "update contacts_table set number = ? where number = ?"
                values = (newno, numb)
                cur.execute(data_update, values)
                mydb.commit()
                print("Record Updated!")
        elif choice == '3':
            newad = input("Enter new address\n")
            data_update = "update contacts_table set address = ? where number = ?"
            values = (newad, numb)
            cur.execute(data_update, values)
            mydb.commit()
            print("Record Updated!")
        elif choice == '4':
            newem = input("Enter new address\n")
            data_update = "update contacts_table set email = ? where number = ?"
            values = (newem, numb)
            cur.execute(data_update, values)
            mydb.commit()
        else:
            print("Exited")

    else:
        print("Record not found!")


def delete_rec():
   
    nmb = input("Enter phone number of contact\n")
    data_fetch = "select * from contacts_table where number = ?"
    cur.execute(data_fetch, (nmb,))
    result = cur.fetchall()  
    if result:
        data_delete = "delete from contacts_table where number = ?"
        cur.execute(data_delete, (nmb,))
        mydb.commit()
        print("Record Deleted!")
    else:
        print("Record not found!")