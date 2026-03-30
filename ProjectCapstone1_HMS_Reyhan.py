#!/usr/bin/env python
# coding: utf-8

# In[104]:


import getpass
import sys

#dictionary 
rooms = [
    {"room_number": "101", "type": "Single", "price": 100000, "status": "Available"},
    {"room_number": "102", "type": "Double", "price": 150000, "status": "Occupied", "guest": "John", "nights": 2},
    {"room_number": "103", "type": "Suite", "price": 250000, "status": "Available"}
]

#set
room_types = {
    "Single", 
    "Double", 
    "Suite"
}

#dictionary 
booking_history = [
    {"room_number": "102", 
     "type": "Double", 
     "guest": "Rey", 
     "nights": 3, 
     "total": 450000}
]

#tuple fix data
hotel_info = (
    "Capstone Hotel", 
    "Bali", 
    3
)

#dictionary 
users = {
    "admin": "admin"
}

#login func
def login():
    print("=== LOGIN SYSTEM ===")
    attempts = 3

    while attempts > 0:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if username in users and users[username] == password:
            print("Login successful!\n")
            return username
        else:
            attempts -= 1
            print(f"Username atau Password yang anda masukkan salah! Percobaan tersisa: {attempts}")

    print("Verifikasi telah melebihi batas maksimal, silahkan coba kembali")
    sys.exit()

#menu input validation func
def input_validation(prompt, min_val, max_val):
    while True:
        choice = input(prompt)
        if choice.isdigit() and min_val <= int(choice) <= max_val:
            return choice
        print(f"Please enter a number between {min_val}-{max_val}")

#number input validation func
def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a valid number")

#add room func
def add_room():
    print("\n--- Add Room ---")
    room_number = get_valid_number("Enter room number: ")

    while True:
        room_type = input("Room type (Single/Double/Suite): ")
        if room_type in room_types:
            break
        print("Invalid room type! Choose: Single / Double / Suite")

    price = get_valid_number("Enter price: ")

    rooms.append({
        "room_number": room_number,
        "type": room_type,
        "price": price,
        "status": "Available"
    })

    print("Room added!")

#view rooms func
def view_rooms(rooms):
    print("\n--- View Rooms ---")
    print("=" * 65)
    print(f"{'Room':<10}{'Type':<10}{'Price':<12}{'Status':<12}{'Guest':<10}{'Stay Period':<3}")
    print("=" * 65)

    for r in rooms:
        guest = r.get("guest", "-")
        night = r.get("nights", "-")
        print(f"{r['room_number']:<10}{r['type']:<10}Rp{r['price']:<10}{r['status']:<12}{guest:<10}{night:<3}")

    print("=" * 65)

#update room func
def update_room():
    print("\n--- Update Rooms ---")
    while True:
        print("\nRoom List:")
        view_rooms(rooms)

        rn = rn = get_valid_number("Room number to update: ")
        rn = str(rn)


        room_found = False
        #find room
        for r in rooms:
            if str(r["room_number"]) == rn:
                room_found = True

                #update room number
                new_rn = get_valid_number("New room number: ")
                r["room_number"] = str(new_rn)

                #update room type
                while True:
                    new_type = input("New room type (Single/Double/Suite): ")
                    if new_type in room_types:
                        r["type"] = new_type
                        break
                    print("Invalid room type! Choose: Single / Double / Suite")

                # Update price
                r["price"] = get_valid_number("New price: ")

                print("Room updated!")
                break

        if not room_found:
                print("Room not found. Try again.")
                continue

        break

#delete room func
def delete_room():
    print("\n--- Delete Rooms ---")
    while True:
        print("\nRoom List:")
        view_rooms(rooms)
        rn = str(get_valid_number("Room number to delete: "))

        for r in rooms:
            if r["room_number"] == rn:
                rooms.remove(r)
                print("Room deleted!")
                break
        else:
            print("Room not found. Try again")
            continue

        break

#room management func
def room_management():
    while True:
        print("\n--- ROOM MANAGEMENT ---")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Update Room")
        print("4. Delete Room")
        print("5. Back")

        sub_input = input_validation("Choose option: ", 1, 5)

        if sub_input == "1":
            add_room()

        elif sub_input == "2":
            print("\nRoom List:")
            view_rooms(rooms)

        elif sub_input == "3":
            update_room()

        elif sub_input == "4":
            delete_room()

        elif sub_input == "5":
            break

#booking room func
def booking_room():
    print("\n--- Room Reservation ---")
    while True:
        print("\nRoom List:")
        view_rooms(rooms)
        rn = str(get_valid_number("Room number: "))

        for r in rooms:
            if r["room_number"] == rn:
                if r["status"] == "Occupied":
                    print("Already occupied!")
                    break

                r["guest"] = input("Guest name: ")
                r["nights"] = get_valid_number("Nights: ")
                r["status"] = "Occupied"

                print("Room booked!")
                break
        else:
            print("Room not found. Try again")
            continue

        break

#occupied room func
def print_occupied_rooms():
    print("\nOccupied Rooms:")
    print("=" * 42)
    print(f"{'Room':<10}{'Type':<10}{'Guest':<10}{'Stay Period':<10}")
    print("=" * 42)

    for r in rooms:
        if r["status"] == "Occupied":
            print(f"{r['room_number']:<10}{r['type']:<10}{r.get('guest','-'):<10}{r.get('nights','-'):<10}")

#booking menu funv
def reservation():
    while True:
        print("\n--- RESERVATION ---")
        print("1. Room Reservation")
        print("2. View Occupied")
        print("3. Back")

        sub_input = input_validation("Choose option: ", 1, 3)

        if sub_input == "1":
            booking_room()

        elif sub_input == "2":
            print_occupied_rooms()

        elif sub_input == "3":
            break

#checkout guest func
def checkout_guest():
    while True:
        print("\n--- GUEST CHECKOUT ---")
        print("\nRoom List:")
        view_rooms(rooms)
        rn = str(get_valid_number("Room number: "))

        for r in rooms:
            if r["room_number"] == rn:
                if r["status"] == "Available":
                    print("Room already empty! Try again.")
                    continue

                nights = r.get("nights", 1)
                total = nights * r["price"]

                print("\n--- CHECKOUT SUMMARY ---")
                print(f"Guest Name         : {r['guest']}")
                print(f"Room Number        : {r['room_number']}")
                print(f"Room Type          : {r['type']}")
                print(f"Stay Duration      : {nights}")
                print(f"Price per night    : Rp {r['price']}")
                print(f"Total Payment      : Rp {total}")
                print("----------------------------")

                booking_history.append({
                    "room_number": rn,
                    "type": r["type"],
                    "guest": r["guest"],
                    "nights": nights,
                    "total": total
                })

                r["status"] = "Available"
                r.pop("guest", None)
                r.pop("nights", None)

                print("Checked out!")
                break
        else:
            print("Room not found. Try again.")
            continue

        break

#checkout menu func
def checkout():
    while True:
        print("\n--- CHECK-OUT ---")
        print("1. Check-Out Guest")
        print("2. Back")

        sub_input = input_validation("Choose option: ", 1, 2)

        if sub_input == "1":
            checkout_guest()

        elif sub_input == "2":
            break

#booking history func
def print_booking_history():
    print("\nBooking History:")
    print("=" * 60)
    print(f"{'Room':<10}{'Type':<10}{'Guest':<15}{'Nights':<10}{'Total':<10}")
    print("=" * 60)

    for b in booking_history:
        print(f"{b['room_number']:<10}{b['type']:<10}{b['guest']:<15}{b['nights']:<10}Rp {b['total']:<10}")

    print("=" * 60)

#print available room func
def print_available_rooms():
    print("\nAvailable Rooms:")
    print("=" * 42)
    print(f"{'Room':<10}{'Type':<10}{'Price':<12}{'Status':<10}")
    print("=" * 42)

    available_rooms = [r for r in rooms if r["status"] == "Available"]
    for r in available_rooms:
        print(f"{r['room_number']:<10}{r['type']:<10}Rp{r['price']:<10}{r['status']:<10}")

    print("=" * 42)
    print(f"Total Available Rooms: {len(available_rooms)}")
    print("=" * 42)

#print total income func
def print_total_income():
    print("\nTotal Income Report:")
    print("=" * 60)
    print(f"{'Room':<10}{'Type':<10}{'Guest':<15}{'Nights':<10}{'Total':<10}")
    print("=" * 60)

    total_income = 0
    for b in booking_history:
        total_income += b["total"]
        print(f"{b['room_number']:<10}{b['type']:<10}{b['guest']:<15}{b['nights']:<10}Rp {b['total']:<10}")

    print("=" * 60)
    print(f"{'Grand Total Income:':<47}Rp {total_income}")
    print("=" * 60)

#report func
def report():
    while True:
        print("\n--- REPORT ---")
        print("1. Rooms List")
        print("2. Available Rooms")
        print("3. Total Income")
        print("4. Booking History")
        print("5. Back")

        sub_input = input_validation("Choose option: ", 1, 5)

        if sub_input == "1":
            print("\nRoom List:")
            view_rooms(rooms)

        elif sub_input == "2":
            print_available_rooms()

        elif sub_input == "3":
            print_total_income()

        elif sub_input == "4":
            print_booking_history()

        elif sub_input == "5":
            break

#main menu
current_user = login()

print("=" * 60)
print(f"{hotel_info[0].center(60)}")
print("=" * 60)

print(f"\nWelcome to {hotel_info[0]} - {hotel_info[1]} ({hotel_info[2]} stars)")
print(f"Logged in as: {current_user}")

while True:
    print("\n=== MAIN MENU ===")
    print("1. Room Management")
    print("2. Reservation")
    print("3. Check-Out")
    print("4. Report")
    print("5. Exit")

    choice = input_validation("Choose option: ", 1, 5)

    if choice == "1":
        room_management()
    elif choice == "2":
        reservation()
    elif choice == "3":
        checkout()
    elif choice == "4":
        report()
    elif choice == "5":
        print("Goodbye!")
        break

