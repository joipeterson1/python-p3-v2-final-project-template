#!/usr/bin/env python3

from helpers import (
    exit_program, 
    list_chores, 
    find_chores_by_name, 
    create_chore, 
    update_chore, 
    delete_chore, 
    list_house_members, 
    find_house_member_by_name, 
    find_house_member_by_id, 
    create_house_member, 
    # update_house_member, 
    # delete_house_member, 
    # list_chore_by_schedule, 
    # list_chore_by_location, 
    # list_chore_house_member
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_chores()
        elif choice == "2":
            find_chores_by_name()
        elif choice == "3":
            create_chore()
        elif choice == "4":
            update_chore()
        elif choice == "5":
            delete_chore()
        elif choice == "6":
            list_house_members()
        elif choice == "7":
            find_house_member_by_name()
        elif choice == "8":
            find_house_member_by_id()
        elif choice == "9":
            create_house_member()
        # elif choice == "10":
        #     update_house_member()
        # elif choice == "11":
        #     delete_house_member()
        # elif choice == "12":
        #     list_chore_by_schedule()
        # elif choice == "13":
        #     list_chore_by_location()
        # elif choice == "14":
        #     list_chore_house_member()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all chores")
    print("2. Find chores by name")
    print("3. Create a new chore")
    print("4. Update a chore")
    print("5. Delete a chore")
    print("6. List all House Members")
    print("7. Find House Members by name")
    print("8. Find House Members by id")
    print("9. Create a new House Member")
    # print("10. Update a House Member")
    # print("11. Delete a House Member")
    # print("12. List all chores by schedule")
    # print("13. List all chores by location")
    # print("14. List all House Members per chore")


if __name__ == "__main__":
    main()
