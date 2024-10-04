#!/usr/bin/env python32
from models.chore import Chore
from models.house_member import Housemember

# def exit_program():
#     print("Exiting the program...")
#     exit()

# def list_chores():
#     chores = Chore.get_all()
#     for chore in chores:
#         print(chore)

# def find_chores_by_name():
#     name = input("Enter the name of the Chore: ")
#     chore = Chore.find_by_name(name)
#     print(chore) if chore else print(
#         f'Oops! {name} is not on the list.'
#     )

# def find_chores_by_id():
#     id_ = input("Enter the ID of the Chore: ")
#     chore = Chore.find_by_id(id_)
#     print(chore) if chore else print(
#         f'Oops! {id_} does not exist.'
#     )

# def create_chore():
#     name = input("Enter the name of the chore: ")
#     schedule = input("Enter the chore's schedule (MWF, TuTh, SaSu, Everyday, As Needed): ")
#     location = input("Enter the chore's location (Laundry Room, Kitchen, Bedroom, Front Yard, Back Yard, Bathroom, Upstairs, Everywhere): ")
#     try:
#         chore = Chore.create(name, schedule, location)
#         print(f'{chore} was added :( ...')
#     except Exception as exc:
#         print("Error creating chore: ", exc)

# def update_chore():
#     id_ = input("Enter the chore's ID that needs to be updated: ")
#     if chore:= Chore.find_by_id(id_):
#         try:
#             name = input("Enter the chore's new name: ")
#             chore.name = name
#             schedule = input("Enter the chore's new schedule: ")
#             chore.schedule = schedule
#             location = input("Enter the chore's new location: ")
#             chore.location = location
            
#             chore.update()
#             print(f'{chore} has been updated!')
#         except Exception as exc:
#             print("Error updating the chore: ", exc)
#     else:
#         print(f'Chore {id_} is not on the list.')

# def update_chore_ids():
#     chores = Chore.get_all()
#     sorted_chores = sorted(chores, key=lambda chore: chore.id)
#     for id, chore in enumerate(sorted_chores, start=1):
#         chore.id = id
#         chore.update()

#     chores = {chore.id: chore for chore in sorted_chores}

#     # not working asked about it in review session.

# def delete_chore():
#     id_ = input("Enter the ID of the chore you want to delete: ")
#     if chore:= Chore.find_by_id(id_):
#         chore.delete()
#         print(f'Good News! we have a maid for Chore {id_} now!')
#         update_chore_ids() 
#     else:
#         print(f'Chore {id_} is not on the list.')

# def list_house_members():
#     house_members = Housemember.get_all()
#     for house_member in house_members:
#         print(house_member)

# def find_house_member_by_name():
#     name = input("Enter the name of the House Member: ")
#     house_member = Housemember.find_by_name(name)
#     print(house_member) if house_member else print(
#         f'{name}? Sorry, never heard of them...'
#     )

# def find_house_member_by_id():
#     id = input("Enter the ID of the House Member: ")
#     house_member = Housemember.find_by_id(id)
#     print(house_member) if house_member else print(
#         f'Oops! House Member {id} not found'
#     )

# def create_house_member():
#     name = input("Enter the name of the member: ")
#     age = int(input("Enter the house member's age: "))
#     chore_id = int(input("Enter the house member's chore ID: "))
#     try:
#         house_member = Housemember.create(name, age, chore_id)
#         print(f'Yay! {house_member.name} is old enough to do chores now!')
#     except Exception as exc:
#         print("Error adding house member: ", exc)

# def update_house_member():
#     id_ = input("Enter the house member's ID that needs to be updated: ")
#     if house_member:= Housemember.find_by_id(id_):
#         try:
#             name = input("Enter the House Member's new name: ")
#             house_member.name = name
#             chore_id = int(input("Enter the House Member's new chore ID: "))
#             house_member.chore_id = chore_id
            
#             house_member.update()
#             print(f'{house_member.name} has been updated!')
#         except Exception as exc:
#             print("Error updating the house member: ", exc)
#     else:
#         print(f'Sorry, House Member {id_} does not have a chore assignment.')

# def delete_house_member():
#     id_ = input("Enter the ID of the House Member that moved out: ")
#     if house_member:= Housemember.find_by_id(id_):
#         house_member.delete()
#         Housemember.renumber_ids()
#         print(f'{house_member.name} has moved out.')
#     else:
#         print(f'House Member {id_} does not have a chore assignment.')

# def list_chore_by_schedule():
#     schedule = input("Enter the schedule of the Chores: ")
#     chore = Chore.find_by_schedule(schedule)
#     print(chore) if chore else print(
#         f'There is no chore with this schedule'
#     )

# def list_chore_by_location():
#     location = input("Enter the location of the Chores: ")
#     chore = Chore.find_by_location(location)
#     print(chore) if chore else print(
#         f'No chore is required for that location'
#     )

# def list_chore_house_member():
#     chore_id = int(input("Enter the chore's ID: "))
#     chore = Chore.find_by_id(chore_id)
#     if chore:
#         house_members = chore.house_members()
#         for house_member in house_members:
#             print(house_member)
#     else:
#         print(f'Chore {chore_id} is not on the list')
