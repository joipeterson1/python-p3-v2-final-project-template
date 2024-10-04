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
                            main_menu()
                        elif housemember_choice == "3":
                            exit_program()
                        else:
                            print("Invalid Choice!")

                    elif chore_choice == "2":
                        main_menu()
                    elif chore_choice == "3":
                        exit_program()
                    else:
                        print("Invalid Choice!")
                chores_detail_menu_()


            elif chore_list_choice == "2":
                main_menu()
            elif chore_list_choice == "3":
                exit_program()
            else:
                print("Invalid Choice!")


        elif choice == "2":
            create_chore()
        elif choice =="3":
            update_chore()
        elif choice == "4":
            delete_chore()
        elif choice == "5":
            chore_details()

            chore_details_menu()
            chores_detail_menu_()

        elif choice =="6":
            list_schedule()

            chore_schedule_menu()
            schedule_choice = input("> ")
            if schedule_choice == "1":
                main_menu()
            elif schedule_choice == "2":
                exit_program()
            else:
                print("Invalid Choice!")

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
    print("5. Select a chore for more details.")
    print("6. See the full chore schedule.")
    print("7. Exit")


def chore_list_menu():
    print("1. Select a chore for more details.")
    print("2. Back to the main menu.")
    print("3. Exit")

def chore_details_menu():
    print("1. See all the House members.")
    print("2. Back to the main menu.")
    print("3. Exit")


def housemember_menu():
    print("1. Select a house member to see more details.")
    print("2. Back to the main menu.")
    print("3. Exit")


def chore_schedule_menu():
    print("1. Back to the main menu.")
    print("2. Exit")    



# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             list_chores()
#         elif choice == "2":
#             find_chores_by_name()
#         elif choice == "3":
#             find_chores_by_id()
#         elif choice == "4":
#             create_chore()
#         elif choice == "5":
#             update_chore()
#         elif choice == "6":
#             delete_chore()
#         elif choice == "7":
#             list_house_members()
#         elif choice == "8":
#             find_house_member_by_name()
#         elif choice == "9":
#             find_house_member_by_id()
#         elif choice == "10":
#             create_house_member()
#         elif choice == "11":
#             update_house_member()
#         elif choice == "12":
#             delete_house_member()
#         elif choice == "13":
#             list_chore_by_schedule()
#         elif choice == "14":
#             list_chore_by_location()
#         elif choice == "15":
#             list_chore_house_member()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit")
#     print("1. List all chores")
#     print("2. Find chores by name")
#     print("3. Find chores by ID")
#     print("4. Create a new chore")
#     print("5. Update a chore")
#     print("6. Delete a chore")
#     print("7. List all House Members")
#     print("8. Find House Members by name")
#     print("9. Find House Members by ID")
#     print("10. Create a new House Member")
#     print("11. Update a House Member")
#     print("12. Delete a House Member")
#     print("13. List all chores by schedule")
#     print("14. List all chores by location")
#     print("15. List all House Members per chore")


if __name__ == "__main__":
    main()
