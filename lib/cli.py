#!/usr/bin/env python3

from helpers import (
    exit_program, 
    list_chores, 
    find_chores_by_name, 
    find_chores_by_id,
    create_chore, 
    update_chore, 
    delete_chore, 
    list_house_members, 
    find_house_member_by_name, 
    find_house_member_by_id, 
    create_house_member, 
    update_house_member, 
    delete_house_member, 
    list_chore_by_schedule, 
    list_chore_by_location, 
    list_chore_house_member
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
            find_chores_by_id()
        elif choice == "4":
            create_chore()
        elif choice == "5":
            update_chore()
        elif choice == "6":
            delete_chore()
        elif choice == "7":
            list_house_members()
        elif choice == "8":
            find_house_member_by_name()
        elif choice == "9":
            find_house_member_by_id()
        elif choice == "10":
            create_house_member()
        elif choice == "11":
            update_house_member()
        elif choice == "12":
            delete_house_member()
        elif choice == "13":
            list_chore_by_schedule()
        elif choice == "14":
            list_chore_by_location()
        elif choice == "15":
            list_chore_house_member()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. List all chores")
    print("2. Find chores by name")
    print("3. Find chores by ID")
    print("4. Create a new chore")
    print("5. Update a chore")
    print("6. Delete a chore")
    print("7. List all House Members")
    print("8. Find House Members by name")
    print("9. Find House Members by ID")
    print("10. Create a new House Member")
    print("11. Update a House Member")
    print("12. Delete a House Member")
    print("13. List all chores by schedule")
    print("14. List all chores by location")
    print("15. List all House Members per chore")


if __name__ == "__main__":
    main()
