#!/usr/bin/env python3

from helpers import(
    list_chores,
    create_chore,
    update_chore,
    delete_chore,
    chore_details,
    list_schedule,
    list_housemembers,
    housemember_details,
    create_house_member,
    update_house_member,
    delete_house_member,
    exit_program,
)

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "1":
            list_chores()

            chore_list_menu()
            chore_list_choice = input("> ")
            if chore_list_choice == "1":
                chore_details()

                def chores_detail_menu_():
                    chore_details_menu()
                    chore_choice = input("> ")
                    if chore_choice == "1":
                        list_housemembers()

                        housemember_menu()
                        housemember_choice = input("> ")
                        if housemember_choice == "1":
                            housemember_details()
                        elif housemember_choice == "2":
                            create_house_member()
                        elif housemember_choice == "3":
                            update_house_member()
                        elif housemember_choice == "4":
                            delete_house_member()
                        else:
                            print("Invalid Choice!")

                    else:
                        print("Invalid Choice!")
                chores_detail_menu_()

            else:
                print("Invalid Choice!")


        elif choice == "2":
            create_chore()
        elif choice =="3":
            update_chore()
        elif choice == "4":
            delete_chore()
        elif choice =="5":
            list_schedule()
        elif choice == "6":
            list_housemembers()
            housemember_menu()
        elif choice == "7":
            exit_program()
        else:
            print("Invalid Choice!")

            # *********** MENUS ************

def main_menu():
    print("Please select an option:")
    print("1. List all chores")
    print("2. Add a new chore")
    print("3. Update a chore")
    print("4. Delete a chore")
    print("5. See the full chore schedule.")
    print("6. See all house members.")
    print("7. Exit")


def chore_list_menu():
    print("1. More details.")

def chore_details_menu():
    print("1. See all house members.")


def housemember_menu():
    print("1. House member details.")
    print("2. Add a new house member.")
    print("3. Update a house member.")
    print("4. Delete a house member.")
   

