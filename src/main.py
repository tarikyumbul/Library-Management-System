
# DICTIONARIES

admin_credentials = {"admin": "123"}  # < A dictionary to store admin credentials. | Login
student_credentials = {"Ahmet": "1234", "Ayse": "4567"}  # < A dictionary to store user credentials. | Login,
                                                         # Creating, Deleting and Listing Users

all_books = [
    ["Book ID: 001,", "Book Name:", "Biology", ", Book Author(s): ", "Alice, Bob", "Number of Copies:", "2"],
    ["Book ID: 002,", "Book Name:", "Chemistry", ", Book Author(s): ", "Alice", "Number of Copies:", "1"],
]  # ^ A dictionary to store all books as lists. | Adding, Modifying, Deleting, Listing Books

book_ids = {"001": all_books[0], "002": all_books[1]}  # < A dictionary to bind book IDs to book lists. | Accessing
                                                       # Books
book_names = {"Biology": [all_books[0]], "Chemistry": [all_books[1]]}  # < A dictionary to bind book names to book
                                                                       # lists. | Accessing Books

authors_to_books = {"Alice": [all_books[0], all_books[1]], "Bob": [all_books[0]]}  # < A dictionary to bind authors
                                                                                   # to their books. | Accessing Books
ids_to_authors = {"001": ["Alice", "Bob"], "002": ["Alice"]}  # < A dictionary to bind book IDs to authors. |
                                                              # Accessing Authors

users_borrowed = {"Ahmet": ["001"], "Ayse": ["002"]}  # < A dictionary to bind users with the books they have
                                                      # borrowed. | Accessing Borrowed Books
borrowed_books = {"001": ["Ahmet"], "002": ["Ayse"]}  # < A dictionary to bind borrowed books with users. | Accessing
                                                      # Users Borrowed a Book
my_books_list = {"Ahmet": [], "Ayse": ["001", "002"]}  # < A dictionary to bind users with the books they have added
                                                       # to their My Books List | Accessing Books

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def library_management_system():  # < The one and only function.

    # LOGIN

    succ_log_att = 0  # < Successful login attempts
    number_of_books = 2  # < Number of books registered at the beginning

    print("\nPlease enter your login information below.\n")

    while succ_log_att < 1:  # < Stops the loop when someone successfully logs in.

        login_username = input("> Username: ")

        if login_username in admin_credentials:

            while succ_log_att < 1:
                login_password = input("> Password: ")

                if login_password == admin_credentials[login_username]:
                    print("\nYou successfully logged in with an admin account.")
                    succ_log_att += 1
                # ^ Checks if the valid username entered above matches the password bound to it.
                else:
                    print("\nInvalid password. Please try again.\n")
                    continue
                # ^ If the password is incorrect it asks again only the password.
            # ^ A second loop for entering password. So you do not have to enter a username after entering an
            # incorrect password.
        # ^ Checks if the username entered exists in admin_credentials.

        elif login_username in student_credentials:

            while succ_log_att < 1:
                login_password = input("> Password: ")

                if login_password == student_credentials[login_username]:
                    print("\nYou successfully logged in with a user account.")
                    succ_log_att += 1
                # ^ Checks if the password entered is correct for the username entered above.
                else:
                    print("\nInvalid password. Please try again.\n")
                    continue
                # ^ If the password is incorrect it asks again only the password.
        # ^ Student Login. Checks if the username entered exists in student_credentials.

        else:
            print("\nInvalid username. Please try again.\n")
            continue
        # ^ If the username is neither in the admin nor in the user credentials lists, it asks again for a username.

        log_out = 0

        while log_out < 1:  # < A loop for logging out

            # ADMIN ACTIONS

            if (login_username in admin_credentials) and (login_password == admin_credentials[login_username]):
            # ^ If the user logged in with an admin account.
                print("\nPlease choose one of the actions below.\n")
                print("1-List books\n2-Create a book\n3-Clean a book\n4-Search for a book\n5-Change number of "
                      "copies of a book by ID\n6-Show students borrowed a book by ID\n7-List Users by ID\n8-Create "
                      "User\n9-Delete User\n10-Exit\n")
                choice = input("> Your Choice: ")
            # ^ If the username and the password are entered correctly for an admin account, this part will be
            # executed. It says "Local variable 'login_password' might be referenced before assignment." but it
            # has no effect

    # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 1 - LISTING ALL CURRENT BOOKS

                if choice == "1":
                # ^ If the user chooses "1" from the list above, this part will be executed.
                    if all_books == []:  # < If there are no books left.
                        print("\nThere are no books in the list.")

                    else:  # < If there are books in the system.
                        print("\n<———List of Books———>\n")
                        book_number = 1  # Book numbers when listing.
                        for book in all_books:
                            print(str(book_number) + ". " + " ".join(book[:4]) + str((book[4]).split(", ")) + ", " +
                                  " ".join(book[5:]))
                            # ^ This is basically for printing a book in exactly or almost the same way shown in the
                            # instructions. This printing method will be used along all the program. Sometimes missing
                            # some cosmetic, but the core part is always the same. It uses ".join" to combine the
                            # elements of the book lists and ".split" to make the authors look like the given in
                            # instructions.
                            book_number += 1
                        # ^ A loop for iterating for every book in all_books. So it will list all the books one by one.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 2 - ADDING A BOOK

                elif choice == "2":
                # ^ If the user chooses "2" from the actions list, this part will be executed.
                    print("\n<———Adding a Book———>\n")
                    name = input("> The Name of the Book: ")

                    exit = 0
                    unique_id = 0
                    while unique_id < 1:
                        if exit == 1:
                            break
                        # ^ This is for going to main menu when the user cancels the action by entering "N" or "n" in
                        # the next section. This is a requirement since there are 2 loops.
                    # ^ When a unique ID is entered for the book, this loop will finish its work.

                        else:
                            id = input("> The ID of the Book (Must Be Unique): ")
                        # ^ This is just the normal process of this part.
                            if id in book_ids:
                                print("\nPlease enter a unique ID.\n")
                            # ^ If the entered ID is in book_ids, it means it is not unique, it asks for another one.
                            elif id == 0:
                                print("Please enter an ID other than 0.")
                            # ^ "0" cannot be an ID for books because in some other parts, it asks user to enter a book
                            # ID to do the action or "0" to go to main menu.
                            else:
                                author = input("> Author(s) of the Book: ")  # Multiple authors should be entered in
                                                                             # this pattern: "Xxxxx, Yyyyy"
                                copies = input("> Number of Copies: ")
                            # ^ If there are no problems, normal process continues.

                                validly_sure = 0
                                while validly_sure < 1:  # < A loop for making it possible to say if the user entered a
                                                         # valid input for the question just below.

                                    sure = str(input("> Are you sure?(Y/N): "))

                                    if sure == "Y" or sure == "y":  # < If the user is sure, the new book is added to
                                                                    # a variety of lists and dictionaries.
                                        number_of_books += 1
                                        # ^ Number of books at the beginning increases by 1 since we add a book. This
                                        # is for being able to add that number correctly -> "all_books[number]"
                                        # See below.

                                        all_books.append(["Book ID: " + id + ",", "Book Name: ", name,
                                                          ", Book Author(s): ", author, "Number of Copies:", copies])
                                        # ^ Adding the book to "all_books" as a list.

                                        book_names[name] = [all_books[number_of_books - 1]]
                                        # ^ Adding the book to "book_names". "number_of_books" is used like this.

                                        book_ids[id] = all_books[number_of_books - 1]
                                        # ^ Adding the book to "book_ids", "number_of_books" is used.

                                        authors_to_books[author] = [all_books[number_of_books - 1]]
                                        # ^ Adding the author of the book to "authors_to_books" and binding it with the
                                        # book.

                                        ids_to_authors[id] = [author]
                                        # ^ Adding the book's ID to "ids_to_authors" and binding it with the author of
                                        # the book.

                                        print("\nThe following book has been added to the library.")
                                        print(" ".join(all_books[number_of_books - 1][:4]) + str((all_books
                                        [number_of_books - 1][4]).split(", ")) + ", " + " ".join(all_books
                                        [number_of_books - 1][5:]))
                                        # ^ Printing the added book. Same method before, just missing list numbers.

                                        validly_sure += 1  # < — Stopping both loops. Adding a book is complete.
                                        unique_id += 1     # < /

                                    elif sure == "N" or sure == "n":
                                        print("\nThe action is canceled.")
                                        exit += 1
                                        break
                                    # ^ If the user wants to cancel the action. "break" is for stopping "while validly_
                                    # sure < 1" and "exit" increases by 1 to stop "while exit < 1".

                                    else:
                                        print("\nPlease enter a valid input.\n")
                                    # ^ If the user enters something other than "Y, y, N, n".

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 3 - DELETING A BOOK

                elif choice == "3":
                # ^ If the user chooses "3" from the actions list, this part will be executed.
                    print("\n<———Deleting a Book———>\n")
                    book_number = 1
                    for book in all_books:
                        print(str(book_number) + ". " + " ".join(book[:4]) + str((book[4]).split(", ")) + ", " +
                              " ".join(book[5:]))
                        book_number += 1
                    # ^ Listing all books. Exactly the same with the one in "Action 1".

                    valid = 0
                    while valid < 1:

                        book_to_delete = input("\n> Enter a book ID to delete a book (Enter 0 to go to the main "
                                               "menu): ")

                        if book_to_delete in book_ids: # < Checks if the book ID entered by the user exists in
                                                       # "book_ids". If so, executes this part.
                            deleted_book = book_ids[book_to_delete]  # < Saving book before deleting it so it can print
                                                                     # it afterwards.
                            author_number = 0
                            for i in ids_to_authors[book_to_delete]:
                            # ^ This loop iterates for every author of the book.

                                authors_to_books[ids_to_authors[book_to_delete][author_number]].remove(book_ids
                                [book_to_delete])
                                # ^ This is basically converting a book's ID to the book itself in "authors_to_books"
                                # and deleting it.

                                if authors_to_books[ids_to_authors[book_to_delete][author_number]] == []:
                                    authors_to_books.pop(ids_to_authors[book_to_delete][author_number])
                                # ^ After that deletion, if there are no books left of the author, author is deleted
                                # too.
                                else:
                                    pass
                                # ^ If there are books left of the author.

                                author_number += 1  # Stops the author based for loop.

                            book_names.pop(book_ids[book_to_delete][2])
                            # ^ Converts book's ID to its name and deletes it from "book_names".
                            all_books.remove(book_ids[book_to_delete])
                            # ^ Converts book ID to book's list and deletes it from "all_books".
                            book_ids.pop(book_to_delete)
                            # ^ Deletes book's ID from "book_ids".
                            if book_to_delete in borrowed_books:
                            # ^ If the book is borrowed by someone before, it will be in "borrowed_books".
                                user_number = 0
                                for user in users_borrowed:
                                # ^ Iterates for every user in "users_borrowed".
                                    if user in borrowed_books[book_to_delete]:
                                    # ^ If the user exists in the book's borrowed users list.
                                        if book_to_delete in users_borrowed[borrowed_books[book_to_delete]
                                        [user_number]]:
                                        # ^ This basically converts the book's ID to the users borrowed it and checks
                                        # if the book exists in those users' borrowed books lists.
                                            users_borrowed[borrowed_books[book_to_delete][user_number]].remove \
                                            (book_to_delete)
                                            # ^ Does the thing above again and deletes the book from "users_borrowed"
                                            # this time.
                                            user_number += 1  # < Increases "user_number" by 1. It is used in those 2
                                                              # just above.

                                        else:
                                            pass

                                    else:
                                        pass

                                borrowed_books.pop(book_to_delete)
                                # ^ Deletes the book from "borrowed_books" if it exists in it.

                            else:
                                pass

                            number_of_books -= 1  # "number_of_books" decrases by 1 since a book is deleted.

                            print("\nThe following book has been deleted from the library.")
                            print(" ".join(deleted_book[:4]) + str((deleted_book[4]).split(", ")) + ", " +
                                  " ".join(deleted_book[5:]))
                            # ^ Prints the book by using the variable saved at the beginning. Same method I use for
                            # printing books.

                            deleted_book = None  # < Deletes the book completely. There is nothing left.

                            valid += 1  # < Stops the loop. Deleting is finished.

                        elif book_to_delete == "0":
                            valid += 1
                        # ^ If the user quits and wants to go to the main menu.

                        elif (book_to_delete not in book_ids) and (book_to_delete != "0"):
                            print("Please enter a valid input.")
                        # ^ If the input for book ID is neither a book ID nor 0.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 4 - SEARCHING FOR A BOOK

                elif choice == "4":
                # ^ If the user chooses "4" from the actions list, this part will be executed.

                    valid_input = 0
                    while valid_input < 1:
                    # ^ Loops until a valid input is entered and the action is completed.
                        name = input("> Enter a book's or its author's full name to search (Enter 0 to go to main "
                                     "menu): ")


                        # Searching With A Book Name

                        if name in book_names:
                        # ^ If the input is a book name.
                            print("\n<———Search Results———>\n")
                            print(" ".join(book_names[name][0][:4]) + str((book_names[name][0][4]).split(", ")) +
                                  ", " + " ".join(book_names[name][0][5:]))
                            # ^ Prints the book that has exactly the same name with the input. Same method for printing
                            # books.
                            valid_input += 1


                        # Searching With An Author Name

                        elif name in authors_to_books:
                        # If the input is an author name.
                            print("\n<———Search Results———>\n")
                            the_book = 0  # < For listing all the books of the author, one by one.
                            book_number = 1
                            for book in authors_to_books[name]:
                                print(str(book_number) + ". " + " ".join(authors_to_books[name][the_book][:4])
                                      + str((authors_to_books[name][the_book][4]).split(", ")) +
                                      ", " + " ".join(authors_to_books[name][the_book][5:]))
                                # ^ Prints the books in the given pattern. Same method for printing books.
                                the_book += 1
                                book_number += 1
                            # ^ Iterates for every book in the author's books list.
                            valid_input += 1  # Action is complete.

                        elif name == "0":
                            valid_input += 1
                        # ^ The user wants to go to the main menu.

                        else:
                            print("\nNothing is found. Please try again.\n")
                        # ^ Input doesn't match a book name, an author name or "0".

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 5 - CHANGING NUMBER OF COPIES

                elif choice == "5":
                # ^ If the user chooses "5" from the actions list, this part will be executed.
                    print("<———List of Books———>\n")
                    book_number = 1
                    for book in all_books:
                        print(str(book_number) + ". " + " ".join(book[:4]) + str((book[4]).split(", ")) + ", " +
                              " ".join(book[5:]))
                        book_number += 1
                    # ^ Listing books. Same as before.

                    valid_id = 0
                    while valid_id < 1:
                    # ^ Requires a valid ID to stop.

                        book_to_change = input("\n> Book ID (Enter 0 to go to main menu): ")

                        if book_to_change in book_ids:
                        # ^ If the book to modify exists in tha library.

                            sufficient_copies = 0
                            while sufficient_copies < 1:
                            # ^ Requires a sufficient amount of copies.

                                new_no_of_copies = int(input("> New Number of Copies: "))

                                borrowed_copies = 0
                                for user in borrowed_books[book_to_change]:
                                    borrowed_copies += 1
                                # ^ Calculates the amount of copies borrowed currently for a given book.

                                if new_no_of_copies >= borrowed_copies:
                                    book_ids[book_to_change][6] = str(new_no_of_copies)
                                    # ^ Changes the amount with the new one.
                                    print("\nThe following book has been updated.")
                                    print(" ".join(book_ids[book_to_change][:4]) + str((book_ids[book_to_change]
                                    [4]).split(", ")) + ", " + " ".join(book_ids[book_to_change][5:]))
                                    # ^ Prints the changed book. Same method.
                                    valid_id += 1  # ——————————> These stop the loops. Modifying is complete.
                                    sufficient_copies += 1  # /
                                # ^ If there are sufficient amount of copies present.

                                else:
                                # ^ If the input is not sufficient.
                                    if borrowed_copies == 1:
                                        print("\n1 user is holding this book. Please "
                                              "enter more number of copies than number of copies in use.\n")
                                    # ^ If there is one borrowed copy of the book present.

                                    else:
                                        print("\n" + str(borrowed_copies) + " users are holding this book. Please "
                                        "enter more number of copies than number of copies in use.\n")
                                    # ^ If there are more than 1 borrowed copies of the book.

                        elif book_to_change == "0":
                            break
                        # ^ If the user wants to quit and enters "0".

                        else:
                            print("\nPlease enter a valid ID.")
                        # ^ If the input is neither a book ID nor "0".

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 6 - LIST STUDENTS BORROWED A BOOK

                elif choice == "6":
                # ^ If the user chooses "6" from the actions list, this part will be executed.
                    succ_display = 0  # < Successful display
                    while succ_display < 1:
                    # ^ Stops when the list is successfully displayed.
                        book_to_display = input("> Book ID (Enter 0 to go to main menu): ")
                        if book_to_display in book_ids:
                        # ^ If the chosen book exists in the library.
                            user_number = 0
                            for user in borrowed_books[book_to_display]:
                                user_number += 1
                            # ^ Calculates the borrowers of a book.
                            if user_number == 1:
                            # ^ If only one user is holding the book.
                                print("\nThis user is holding this book:")
                                for user in borrowed_books[book_to_display]:
                                    print("-" + user)
                                # ^ Iterates for every borrower of the book. Only once in this case. But it is an easy
                                # way to get rid of the brackets.
                                succ_display += 1
                            else:
                            # ^ If more than one users are holding the book.
                                print("\nThese users are holding this book:")
                                for user in borrowed_books[book_to_display]:
                                    print("-" + user)
                                # ^ Iterates for every borrower of the book.
                                succ_display += 1

                        elif book_to_display == "0":
                            break
                        # ^ If the user wants to quit and go to the main menu.

                        else:
                            print("\nPlease enter a valid ID.\n")
                        # ^ If the input neither is a book ID nor "0".

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 7 - LISTING USERS

                elif choice == "7":
                # ^ If the user chooses "7" from the actions list, this part will be executed.
                    print("\n<———List of Users———>")
                    number = 1
                    for (user, password) in student_credentials.items():
                        print(str(number) + "-" + user)
                        number += 1
                    # ^ Takes the keys and the values of the "student_credentials" as tuples and prints only the keys,
                    # which are users.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 8 - ADDING A USER

                elif choice == "8":
                # ^ If the user chooses "8" from the actions list, this part will be executed.
                    print("\n<———Adding a User———>\n")
                    new_username = input("Username: ")
                    if new_username not in student_credentials:
                    # ^ If the username taken from the user does not exist in the library.
                        new_password = input("Password: ")
                        student_credentials[new_username] = new_password
                        # ^ Creates a key-value pait in "student_credentials" whose key is the new username and the
                        # value is the password.

                    else:
                        print("\nPlease enter a unique username.")
                    # ^ If the new user's username is already in use.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 9 - DELETING A USER

                elif choice == "9":
                # ^ If the user chooses "9" from the actions list, this part will be executed.
                    print("\n<———Deleting a User———>")
                    number = 1
                    for (user, password) in student_credentials.items():
                        print(str(number) + "-" + user)
                        number += 1
                    # ^ Lists users. Exactly like in action 7.

                    valid_username = 0
                    while valid_username < 1:
                    # ^ Loops until a valid username is entered.
                        user_to_delete = input("\nPlease enter a username: ")
                        if user_to_delete in student_credentials:
                            student_credentials.pop(user_to_delete)
                        # ^ If the user exists in the library. It deletes the user's credentials.
                            if user_to_delete in users_borrowed:
                                users_borrowed.pop(user_to_delete)
                            # ^ If the user ever borrowed a book before, it exists in that dictionary. Deletes the user
                            # from the "users_borrowed".

                            else:
                            # ^ If the user never borrowed a book from the library before.
                                pass

                            for books in borrowed_books:
                            # ^ Iterates for every book in "borrowed_books" list.
                                if user_to_delete in borrowed_books[books]:
                                    borrowed_books[books].remove(user_to_delete)
                                # ^ If the user exists in a book's borrowed users list, it gets deleted.
                                else:
                                    pass

                            print("\nThe user '" + user_to_delete + "' has been successfully deleted.")
                            # ^ Prints the deleted user.
                            user_to_delete = () # < Completely deletes the user. There is nothing left.

                            valid_username += 1 # < Stops the loop. User deletion is finished.


                        else:
                            print("\nPlease enter a valid username.")
                        # ^ If the input does not match any users.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # ADMIN ACTION 10 - EXIT

                elif choice == "10":
                # ^ If the user chooses "10" from the actions list, this part will be executed.
                    print("\nYou successfully logged out.\n")
                    log_out += 1  # < Stops the related loop. Users gets out of actions section.
                    succ_log_att -= 1  # < Starts the related loop. Users gets back to the login screen.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # INVALID INPUT

                else:
                    print("\nPlease choose a valid action.")
                # ^ When the user enters an invalid input for an action. They will be asked to enter again.

    # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

            # STUDENT LOGIN

            elif (login_username in student_credentials) and (login_password == student_credentials[login_username]):
            # ^ If the user logged in with a student account.
                print("\nPlease choose one of the actions below.\n")
                print("1-Search for a book\n2-Add a book to my books list\n3-Delete a book from my books list\n"
                      "4-Show my borrowed books\n5-Exit\n")
                choice = input("> Your Choice: ")

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # STUDENT ACTION 1 - SEARCHING A BOOK

                if choice == "1":
                    # ^ If the user chooses "1" from the actions list, this part will be executed.
                    # This part is exactly the same with admin action 4.
                    valid_input = 0
                    while valid_input < 1:
                    # ^ Loops until a valid input is entered and the action is completed.
                        name = input("> Enter a book's or its author's full name to search (Enter 0 to go to main "
                                     "menu): ")


                        # Searching With A Book Name

                        if name in book_names:
                        # ^ If the input is a book name.
                            print("\n<———Search Results———>\n")
                            print(" ".join(book_names[name][0][:4]) + str((book_names[name][0][4]).split(", ")) +
                                  ", " + " ".join(book_names[name][0][5:]))
                            # ^ Prints the book that has exactly the same name with the input. Same method as before.
                            valid_input += 1


                        # Searching With An Author Name

                        elif name in authors_to_books:
                        # If the input is an author name.
                            print("\n<———Search Results———>\n")
                            the_book = 0  # < For listing all the books of the author, one by one.
                            book_number = 1
                            for book in authors_to_books[name]:
                                print(str(book_number) + ". " + " ".join(authors_to_books[name][the_book][:4])
                                      + str((authors_to_books[name][the_book][4]).split(", ")) +
                                      ", " + " ".join(authors_to_books[name][the_book][5:]))
                                # ^ Prints the books in the given pattern. Same method.
                                the_book += 1
                                book_number += 1
                            # ^ Iterates for every book in the author's books list.
                            valid_input += 1  # Action is complete.

                        elif name == "0":
                            valid_input += 1
                        # ^ The user wants to go to the main menu.

                        else:
                            print("\nNothing is found. Please try again.\n")
                        # ^ Input doesn't match a book name, an author name or "0".


        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # STUDENT ACTION 2 - ADDING A BOOK TO MY BOOKS LIST

                elif choice == "2":
                # ^ If the user chooses "2" from the actions list, this part will be executed.
                    print("\n<———List of Available Books———>\n")
                    book_number = 1
                    for book in all_books:
                        print(str(book_number) + ". " + " ".join(book[:4]) + str((book[4]).split(", ")) + ", " +
                              " ".join(book[5:]))
                        book_number += 1
                    # ^ Lists all books with exactly the same method before.

                    succ_adding = 0  # Successful adding
                    while succ_adding < 1:
                    # Loops until a book is successfuly added.
                        book_to_add = input("\n> Book ID (Enter 0 to go to main menu): ")
                        if (book_to_add not in my_books_list[login_username]) and (book_to_add in book_ids):
                        # If the book that will be added is not already in the My Books list of the current user and
                        # the book exists in the library.
                            number_of_copies = 0
                            for copy_in_use in borrowed_books[book_to_add]:
                                number_of_copies += 1
                            # ^ Calculates the copies in use of the chosen book.
                            if int(book_ids[book_to_add][6]) > number_of_copies:
                                my_books_list[login_username] = my_books_list[login_username] + [book_to_add]
                            # ^ If there are sufficient amount of copies of the chosen book, it adds the book to the
                            # current user's My Books list.
                                print("\nThe book has successfully been added to your list.")
                                succ_adding += 1 # < Stops the loop.

                            else:
                                print("\nThere are no enough copies of that book. Please choose another one.")
                            # ^ If there are no enough copies of the chosen book, the program will tell so.

                        elif (book_to_add not in book_ids) and (book_to_add != "0"):
                            print("\nPlease enter a valid ID.")
                        # ^ If the book ID does not exist in the library and the input is not "0".

                        elif book_to_add == "0":
                            break
                        # ^ If the ınput is "0", the programs returns to main menu.

                        else:
                            print("\nThis book is already in your list. Please choose another one.")
                        # ^ If the previous conditions are false, the only option left is that the user is trying to add
                        # a book which is already in their My Books list.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # STUDENT ACTION 3 - DELETING A BOOK FROM MY BOOKS LIST

                elif choice == "3":
                # ^ If the user chooses "3" from the actions list, this part will be executed.

                    if my_books_list[login_username] != []:
                        print("\n<———List of Books in Your List———>\n")
                    # ^ List books only if the user's My Books list is not empty.
                        book_number = 1
                        for borrowed in my_books_list[login_username]:
                            print(str(book_number) + ". " + " ".join(book_ids[borrowed][:4]) + str((book_ids[borrowed][4]).split(", ")) + ", " +
                                  " ".join(book_ids[borrowed][5:]))
                            book_number += 1
                            # ^ The print method I use for every time a book should be printed. It's the same.
                        # ^ Iterates for every book in the current user's My Books list.

                        valid_input = 0
                        while valid_input < 1:
                        # ^ Stops when a valid input is entered and its action is completed.
                            book_to_return = input("\nBook ID (Enter 0 to go to main menu): ")

                            if book_to_return in my_books_list[login_username]:
                            # ^ Executes if the chosen book exists in the current user's My Books list.
                                print("\nThe following book will be deleted from your list.")
                                print(" ".join(book_ids[book_to_return][:4]) + str((book_ids[book_to_return][4]).
                                split(", ")) + ", " + " ".join(book_ids[book_to_return][5:]))
                                # ^ Same book printing method. Without listing numbers.
                                sure = input("\nAre you sure? (Y/N): ")
                                if sure == "Y" or sure == "y":
                                    my_books_list[login_username].remove(book_to_return)
                                    valid_input += 1
                                # ^ If the user is sure, the book is deleted from their My Books list.

                                elif sure == "N" or sure == "n":
                                    break
                                # ^ If the user quits, the program goes back to main menu.

                                else:
                                    print("Please enter a valid input.")
                                # ^ If the answer is neither yes nor no, it's invalid.

                            elif book_to_return == "0":
                                break
                            # ^ If the input is "0", the program will go back to main menu.

                            else:
                                print("\nPlease enter a valid input.")
                            # ^ If the input is neither a valid book ID nor "0", it's invalid.

                    else:
                        print("\nThere are no books in your list.")
                    # ^ If the current user's My Books list is [], which means it is empty.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # STUDENT ACTION 4 - LIST BORROWED BOOKS

                elif choice == "4":
                 # ^ If the user chooses "4" from the actions list, this part will be executed.
                    if my_books_list[login_username] == []:
                        print("\nThere are no books in your list.")
                    # ^ If the current user has no books in their My Books List, the program will tell so.

                    else:
                    # If the user has book(s) in their My Books list.
                        book_number = 1
                        print("\nYour books: ")
                        for borrowed in my_books_list[login_username]:
                            print(str(book_number) + ". " + " ".join(book_ids[borrowed][:4]) + str(
                            (book_ids[borrowed][4]).split(", ")) + ", " + " ".join(book_ids[borrowed][5:]))
                            book_number += 1
                         # ^ The same method I used to print books all along the program.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # STUDENT ACTION 5 - LOG OUT

                elif choice == "5":
                # ^ If the user chooses "5" from the actions list, this part will be executed.
                    print("\nYou successfully logged out.\n")
                    log_out += 1  # < Stops the related loop. Users gets out of actions section.
                    succ_log_att -= 1  # < Starts the related loop. Users gets back to the login screen.

        # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

                # INVALID INPUT

                else:
                    print("\nPlease choose a valid action.")
                # ^ When the user enters an invalid input for an action. They will be asked to enter again.

    # ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

            else:
                print("Me: This will never happen."
                      "\n*happens*"
                      "\nMe:")
                print("⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿"
                      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿")



library_management_system()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Written By: Hasan Tarık Yumbul
# Student Number: 219171247
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
