#!/usr/bin/env python32
from models.chore import Chore
from models.house_member import Housemember

def space():
    print("")

def line():
    print("_____________________")    

def list_chores():
    chores = Chore.get_all()
    line()
    space()
    print("The House Chore List:")
    for chore in chores:
        print(f"{chore.id}. {chore.name}")
    space()
    line()


def create_chore():
    name = input("Enter the name of the chore: ")
    schedule = input("Enter the chore's schedule (MWF, TuTh, SaSu, Everyday, As Needed): ")
    location = input("Enter the chore's location (Laundry Room, Kitchen, Bedroom, Front Yard, Back Yard, Bathroom, Upstairs, Everywhere): ")
    try:
        chore = Chore.create(name, schedule, location)
        print(f'{chore.name} was added :( ...')
        list_chores()
    except Exception as exc:
        print("Error creating chore: ", exc)

def update_chore():
    list_chores()
    selected_chore = input("Select a chore that needs to be updated: ")
    chore = Chore.find_by_id(selected_chore)
    if chore:
        try:
            name = input("Enter the chore's new name: ")
            chore.name = name
            schedule = input("Enter the chore's new schedule (MWF, TuTh, SaSu, Everyday, As Needed): ")
            chore.schedule = schedule
            location = input("Enter the chore's new location (Laundry Room, Kitchen, Bedroom, Front Yard, Back Yard, Bathroom, Upstairs, Everywhere): ")
            chore.location = location
            
            chore.update()
            space()
            print(f'{chore} has been updated!')
            space()
        except Exception as exc:
            print("Error updating the chore: ", exc)
    else:
        print(f'Chore {selected_chore} is not on the list.')

def update_chore_ids():
    chores = Chore.get_all()
    sorted_chores = sorted(chores, key=lambda chore: chore.id)
    for id, chore in enumerate(sorted_chores, start=1):
        chore.id = id
        chore.update()

    chores = {chore.id: chore for chore in sorted_chores}


def delete_chore():
    list_chores()
    selected_chore = input("Select the chore you want to delete: ")
    chore = Chore.find_by_id(selected_chore)
    if chore:
        chore.delete()
        space()
        print(f'Good News! we have a maid for Chore {selected_chore} now! See the new chore list below!')
        space()
        update_chore_ids()
        list_chores()
    else:
        print(f'Chore {selected_chore} is not on the list.')

def chore_details():
    selected_chore = input("Which chore would you like to select? ")
    chore = Chore.find_by_id(selected_chore)
    if chore:
        space()
        print(f"****** {chore.name} ******")
        print(f"Schedule: {chore.schedule}")
        print(f"Location: {chore.location}")
        space()
        housemembers = chore.house_members()
        for housemember in housemembers:
            print("")
            print("This chore is assigned to:")
            print(f"{housemember.name}!!")
        print("")
    else:
        print("Sorry, the chore you selected is not on the list...")

def list_housemembers():
    housemembers = Housemember.get_all()
    line()
    space()
    print("The House Members:")
    for housemember in housemembers:
        print(f"{housemember.id}. {housemember.name}")
    space()
    line()

def housemember_details():
    selected_housemember = input("Select a house member: ")
    housemember = Housemember.find_by_id(selected_housemember)
    if housemember:
        space()
        print(f"**** Meet {housemember.name}! ****")
        print(f"{housemember.name} is {housemember.age} years old.")
        assigned_chore = Chore.find_by_id(housemember.chore_id)
        if assigned_chore:
            print(f"The chore that {housemember.name} is assigned to is {assigned_chore}.")
            space()
        else:
            print("Chore not found!")
    else:
        print("House member not found!")


def create_house_member():
    name = input("Enter the name of the member: ")
    age = int(input("Enter the house member's age: "))
    selected_chore = (input("Enter the name house member's chore: "))
    chore = Chore.find_by_name(selected_chore)
    if chore:
        chore_id = chore.id
    else:
        print("Chore not found!")
    try:
        house_member = Housemember.create(name, age, chore_id)
        space()
        print(f'Yay! {house_member.name} is old enough to do chores now!')
        space()
    except Exception as exc:
        print("Error adding house member: ", exc)

def update_house_member():
    selected_housemember = int(input("Select the house member that needs to be updated: "))
    if house_member:= Housemember.find_by_id(selected_housemember):
        try:
            name = input("Enter the house member's new name: ")
            house_member.name = name
            selected_chore = (input("Enter the name of the house member's new chore: "))
            chore = Chore.find_by_name(selected_chore)
            if chore:
                chore_id = chore.id
            else:
                print("Chore not found!")
            house_member.chore_id = chore_id
            
            house_member.update()
            space()
            print(f'{house_member.name} has been updated!')
            space()
        except Exception as exc:
            print("Error updating the house member: ", exc)
    else:
        print('Sorry, house member not found!.')

def delete_house_member():
    selected_housemember = int(input("Select the House Member that moved out: "))
    house_member = Housemember.find_by_id(selected_housemember)
    if house_member:
        house_member.delete()
        Housemember.renumber_ids()
        print(f'{house_member.name} has moved out.')
    else:
        print('Sorry, house member not found!.')

def list_schedule():
    chores_mwf = Chore.find_by_schedule("MWF")
    chores_tuth = Chore.find_by_schedule("TuTh")
    chores_sasu = Chore.find_by_schedule("SaSu")
    chores_everyday = Chore.find_by_schedule("Everyday")
    chores_as_needed = Chore.find_by_schedule("As Needed")
    line()
    space()
    print("**** The Chore Schedule ****")
    space()
    print("Mondays, Wednesdays and Fridays: ")
    for chore in chores_mwf:
        print(f"- {chore.name}, Location: {chore.location}")

    space()
    print("Tuesdays and Thursdays: ")
    for chore in chores_tuth:
        print(f"- {chore.name}, Location: {chore.location}")

    space()
    print("Saturdays an Sundays: ")
    for chore in chores_sasu:
            print(f"- {chore.name}, Location: {chore.location}")

    space()
    print("Everyday: ")
    for chore in chores_everyday:
            print(f"- {chore.name}, Location: {chore.location}")

    space()
    print("As Needed: ")
    for chore in chores_as_needed:
            print(f"- {chore.name}, Location: {chore.location}")
    space()
    line()

def exit_program():
    print("Exiting the program...")
    exit()

